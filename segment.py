from extract import extract_all
from DictionaryPrefixTree import DictionaryPrefixTree
from LabelDataPrefixTree import LabelDataPrefixTree
import math
import operator

# Seperate the sentence as a prefix tree structure and return a list.


def sentence_to_prefix_tree_list(max_char, str1):
    sentence_list = list()
    for j in range(1, max_char + 1):
        str2 = str1[0:j]
        if str2 != "":
            sentence_list.append(str2)
    return sentence_list

# Merge 2 small segments into a bigger segment accroding to threshold value measure


def merge(word1, count_word1, word2, count_word2, label_data, len):
    '''
    Determine which one is better, i.e. "嗰陣", "嗰陣時"
    Number of "嗰陣" in label data: 197
    Number of "時" in label data: 614
    Number of "嗰陣時" in label data: 186
    Number of vocab = M (constant value)
    Threshold = μ (constant value, estimated through experiments)
    MI("嗰陣", "時") = log(2, (186 * M) / (197 * 614))
    if MI("嗰陣", "時") >= threshold:
        return Ture -> "嗰陣時"
    else:
        return False -> "嗰陣/時"
    '''
    MI_value = 0
    merged_word = False
    # TODO: By experiment, set threshold = 6 first.
    threshold = 6
    word3 = word2.replace(word1, "")
    count_word3 = 0
    for x in label_data:
        count_word3 += x.count(word3)
    print(word1 + ": " + str(count_word1))
    print(word2 + ": " + str(count_word2))
    print(word3 + ": " + str(count_word3))
    if count_word1 != 0 and count_word2 != 0 and count_word3 != 0:
        total = (count_word2 * len) / (count_word1 * count_word3)
        MI_value = math.log(total, 2)
        print("MI Value:", MI_value)
    if MI_value >= threshold:
        merged_word = True
    return merged_word

# Segment all sentence in the given sentence list,and return a list of segmented sentence


def segment(sentence_list):
    segmentation_result = []
    my_count = 1
    for sentence in sentence_list:
        print(str(my_count) + ": " + sentence)
        my_count += 1
        # Dictionary-based Part
        # Build a Vocab Dictionary Prefix Tree
        dict_trie = DictionaryPrefixTree()

        # Create a file pointer fd,open th vocab dictionary with read-only mode
        with open("dictionary/vocab_dictionary.txt", 'r', encoding='utf-8') as fd:
            dictionary_list = fd.readlines()
            # Remove space appears in all lines of dictionary_list
            dictionary_list = [line.rstrip() for line in dictionary_list]

        # For all vocabs in dictionary_list
        for vocabs in dictionary_list:
            # Insert the words into the DictionaryPrefixTree trie
            dict_trie.insert(vocabs)

        ####### Output1: Print out all vocab in vocab_dictionary which contains in sentence #######
        print("Vocabs contains:")
        # Deal with the non-cantonese issue.
        tmp_sentence = sentence
        for ch in [' ', '.', '。', '?', '？', ',', '，', '<', '《', '>', '》', '、', '\\', '/', '\'', '“', '"', '”', '：', ':', '；', ';', '{', '}', '[', ']', '(', ')', '!', '！', '@', '#', '$', '%', '^', '&', '*', '_', '-', '+', '=', '|']:
            if ch in tmp_sentence:
                tmp_sentence = tmp_sentence.replace(ch, "")
        # print(tmp_sentence)
        vocabs = dict_trie.contains(tmp_sentence)
        print(vocabs)

        # Build a Label Data Prefix Tree
        label_data_trie = LabelDataPrefixTree()
        count_label_data = 0
        # Extract all label data from the datasets
        label_data = extract_all()
        for label_data_list in label_data:
            # Split the label data string
            label_data_split = label_data_list.split()
            # For all vocabs in label_data_list
            for vocabs2 in label_data_split:
                # Insert the words into the LabelDataPrefixTree trie
                label_data_trie.insert(vocabs2)
                # Calculate the number of characters in label data for calculate the MI value -> M
                count_label_data += 1
        #print("count_label_data:", count_label_data)

        sentence_len = len(sentence)
        new_segment = ""
        # TODO We set the maximum number of character in a single word as 5.
        maximum_char = 5
        count = 0
        i = 0
        while i < sentence_len:
            found_vocab = False
            found_label_data = False
            if maximum_char + i < sentence_len:
                str1 = sentence[i:maximum_char+i]
            else:
                str1 = sentence[i:]
            count = 0
            # Split the sentence to prefix tree structure with a maximum of 5 characters
            sentence_list = sentence_to_prefix_tree_list(maximum_char, str1)
            #dictionary_list_len = len(dictionary_list)
            dictionary = {}

            # Get the frequency of each splitted sentence, if no just return 0
            for x in sentence_list:
                dictionary[x] = label_data_trie.get_frequency(x)
            print("frequency:")

            # Sort value found from the dictionary in descending order.
            sorted_dictionary = dict(
                sorted(dictionary.items(), key=operator.itemgetter(1), reverse=True))
            print(sorted_dictionary)

            word_list = []
            index = 0
            first_dict_value = list(sorted_dictionary.values())[0]
            # If the first value of the sorted dictionary is not zero,
            # it means we can at least found one label data
            if first_dict_value != 0:
                found_label_data = True
            # If the key in the sorted dictionary can be found in the
            # vocab dictionary, return true
            for key in sorted_dictionary:
                if vocabs is not None:
                    if key in vocabs:
                        found_vocab = True
                        word_list.append(key)

            if found_vocab == True:
                print("Found vocab in dictionary: ")
                print(word_list)

                # If there are more than one vocab in the dictionary, use MI to measure which one is better
                if len(word_list) > 1:
                    if len(word_list) >= 2:
                        merge_word = merge(word_list[0], sorted_dictionary[word_list[0]], word_list[1],
                                           sorted_dictionary[word_list[1]], label_data, count_label_data)
                        #print("Merge word:", str(merge_word))
                        if merge_word == True:
                            index = 1

                count = len(word_list[index]) - 1
                if sorted_dictionary[word_list[index]] != 0:
                    found_label_data = True
                else:
                    found_label_data = False

            if found_vocab == True and found_label_data == True:
                the_word = word_list[index]
            elif found_vocab == True and found_label_data == False:
                the_word = word_list[index]
            elif found_vocab == False and found_label_data == True:
                # For some cases such as "係", "嘅", just split the most frequently label data.
                the_word = list(sorted_dictionary.keys())[0]
            else:
                the_word = list(sorted_dictionary.keys())[
                    0]  # Out-of-vocabulary(OOV) cases
            print("Found vocab: " + str(found_vocab) +
                  " ,number of vocab: " + str(len(word_list)))
            print("Found label data: " + str(found_label_data))
            i += count
            i += 1
            if i < sentence_len:
                new_segment += the_word + "/"
            else:
                new_segment += the_word
            print(new_segment)
            if i >= sentence_len:
                segmentation_result.append(new_segment)
            print("\n")
    return segmentation_result
