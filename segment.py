from extract import extract_all
from DictionaryPrefixTree import DictionaryPrefixTree
import math
import operator


# Seperate the sentence as a prefix tree structure and return a list.
def sentence_to_prefix_tree_list(max_char, str1):
    sentence_list = list()
    for j in range(1, max_char + 1):
        str2 = str1[0:j]
        #str3 = str1[j:max_char]
        if str2 != "":
            sentence_list.append(str2)
        # if str3 != "":
        #    sentence_list.append(str3)
    return sentence_list


# Merge 2 small segments into a bigger segment accroding to threshold value measure
def merge(dictionary, len):
    MI_value = {}
    merged_word = []
    # TODO: By experiment, set threshold = 5 first.
    threshold = 5
    for key1 in dictionary:
        for key2 in dictionary:
            if key1 + key2 in dictionary:
                merge = key1 + key2
                count1 = dictionary[key1]
                count2 = dictionary[key2]
                merge_count = dictionary[merge]
                print(merge)
                total = (merge_count * len) / (count1 * count2)
                MI_value[merge] = math.log(total, 2)
                if MI_value[merge] >= threshold:
                    merged_word.append(merge)
    return merged_word


# Segment all sentence in the given sentence list,and return a list of segmented sentence
def segment(sentence_list):
    segmentation_result = []
    for sentence in sentence_list:
        # Search it from the dictionary
        dict_trie = DictionaryPrefixTree()

        # Create a file pointer fd,open th vocab_dictionary with read-only mode
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
        vocabs = dict_trie.contains(sentence)
        print(vocabs)

        ####### Output2: Print out all segmentd sentance in label data by prefix trie #######
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
                #print("[" + str(i) + ", " + str(maximum_char+i) + "]")
            else:
                str1 = sentence[i:]
                #print("[" + str(i) + ", " + str(sentence_len) + "]")
            count = 0
            sentence_list = sentence_to_prefix_tree_list(maximum_char, str1)
            label_data = extract_all()
            dictionary = {}
            count_char = 0

            # For each substring, count the number of occurrences in label data.
            for x in sentence_list:
                for y in label_data:
                    count_char += y.count(x)
                dictionary[x] = count_char
                count_char = 0
            print("frequency:")

            # Sort value found from the dictionary in descending order.
            sorted_dictionary = dict(
                sorted(dictionary.items(), key=operator.itemgetter(1), reverse=True))
            print(sorted_dictionary)
            word_list = []
            first_dict_value = list(sorted_dictionary.values())[0]
            if first_dict_value != 0:
                found_label_data = True

            for key in sorted_dictionary:
                if key in vocabs:
                    found_vocab = True
                    word_list.append(key)

            if found_vocab == True:
                print("Found vocab in dictionary: ")
                print(word_list)
                # if len(word_list) > 1:
                # Determine which one is better, i.e. "伊斯蘭", "伊斯蘭教"
                # See whether the substring of "伊斯蘭教" can connect with "教會", i.e. "教".

                count = len(word_list[0]) - 1
                if sorted_dictionary[word_list[0]] != 0:
                    found_label_data = True
                else:
                    found_label_data = False

            if found_vocab == True and found_label_data == True:
                # Should calculate the rating between vocab and label data.
                the_word = word_list[0]
            elif found_vocab == True and found_label_data == False:
                # Should calculate the rating between different vocabs, i.e."大學", "大學生".
                the_word = word_list[0]
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
