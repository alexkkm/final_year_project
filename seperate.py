from extract import extract_all
from DictionaryPrefixTree import DictionaryPrefixTree
# from PrefixTree import PrefixTree
import math
import operator

# Seperate the sentance as a prefix tree structure and return a list.


def seperate(max_char, str1):
    sentence_list = list()
    for j in range(1, max_char + 1):
        str2 = str1[0:j]
        #str3 = str1[j:max_char]
        if str2 != "":
            sentence_list.append(str2)
        # if str3 != "":
        #    sentence_list.append(str3)
    return sentence_list


def merge(dictionary, len):
    MI_value = {}
    merged_word = []
    threshold = 5  # By experiment, set threshold = 5 first.
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


### Example (print out frequency and vocabs of given sentence)  ###
if __name__ == '__main__':

    # Build a PrefixTree called trie
    #trie = PrefixTree()

    # Sentence would like to analysis
    # sentence = "廣東話容唔容易學"

    sentence = "我係大學生幹事會嘅成員"

    sentence1 = "世一中場佐真奴"
    sentence2 = "今天我寒夜裡看雪飄過"
    sentence3 = ""
    sentence4 = "我係一個西伯利亞人"
    sentence5 = "大家都好中意食麥當勞"
    sentence6 = "我老闆想我今晚十點之前做完啲嘢"
    # Forward case. It should output "中國/嘅/伊斯蘭/教會" instead of "中國/嘅/伊斯蘭教/會".
    sentence7 = "中國嘅伊斯蘭教會"
    # Backward case. It should output "/我/係/大學生/幹事/會/嘅/成員" instead of "/我/係/大學/生/幹事/會/嘅/成員".
    sentence8 = "我係大學生幹事會嘅成員"

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
    print()

    ####### Output2: Print out all seperated sentance in label data by prefix trie #######
    sentence_len = len(sentence)
    new_sentence = ""
    # We set the maximum number of character in a single word as 5.
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
        sentence_list = seperate(maximum_char, str1)
        label_data = extract_all()
        label_data_len = len(label_data)
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
        new_sentence += "/" + the_word
        print(new_sentence)

    #   print("Label Data Length:", label_data_len)
    #   dict2 = {'中': 170, '中國': 20, '斯': 300, '國': 144, '教會': 2, '蘭': 200, '嘅': 1606, '教': 96, '會': 830}
    #   print(merge(dict, label_data_len))
