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


# Merge 2 segments accroding to threshold value measure
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

def seperate(sen_list):
    final_sentence = []
    for sentence in sen_list:
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
            sentence_list = sentence_to_prefix_tree_list(maximum_char, str1)
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
            if i < sentence_len:
                new_sentence += the_word + "/"
            else:
                new_sentence += the_word
            print(new_sentence)
            if i >= sentence_len:
                final_sentence.append(new_sentence)

            #   print("Label Data Length:", label_data_len)
            #   dict2 = {'中': 170, '中國': 20, '斯': 300, '國': 144, '教會': 2, '蘭': 200, '嘅': 1606, '教': 96, '會': 830}
            #   print(merge(dict, label_data_len))
    return final_sentence

def f_score(sentence_list, correct_sentence_list):
    new_list1 = []
    new_list2 = []
    number_of_sentence = len(sentence_list)

    for sentence in sentence_list:
        new_sentence = ""
        for i in range(len(sentence)-1):
            if sentence[i] != "/" and sentence[i+1] != "/":
                new_sentence += sentence[i] + "_"
            else:
                new_sentence += sentence[i]
        new_sentence += sentence[len(sentence)-1]
        new_list1.append(new_sentence)
    #print(new_list1)
    
    for correct_sentence in correct_sentence_list:
        new_sentence = ""
        for j in range(len(correct_sentence) - 1):
            if correct_sentence[j] != "/" and correct_sentence[j+1] != "/":
                new_sentence += correct_sentence[j] + "_"
            else:
                new_sentence += correct_sentence[j]
        new_sentence += correct_sentence[len(correct_sentence)-1]
        new_list2.append(new_sentence)
    #print(new_list2)

    # Calculate the precision
    precision = 0
    recall = 0
    for k in range(number_of_sentence):
        count_TP = 0
        count_FP = 0
        count_FN = 0
        sentence1 = new_list1[k]
        sentence2 = new_list2[k]
        for x in range(len(sentence1)):
            if sentence1[x] == "/" and sentence2[x] != "/":
                count_FP += 1 # FP
            if sentence1[x] == "/" and sentence2[x] == "/":
                count_TP += 1 # TP
            if sentence1[x] != "/" and sentence2[x] == "/":
                count_FN += 1 # TP
        precision += count_TP / (count_TP + count_FP)
        recall += count_TP / (count_TP + count_FN)
        print("TP:", count_TP)
        print("FP:", count_FP)
        print("FN:", count_FN)
    precision = precision / number_of_sentence
    recall = recall / number_of_sentence
    f_score = (2 * precision * recall)/(precision + recall)
    print("Precision:", precision)
    print("Recall:", recall)
    print("F-score:", f_score)
    return f_score
    
### Example (print out frequency and vocabs of given sentence)  ###
if __name__ == '__main__':

    sentence1 = "世一中場佐真奴"
    sentence2 = "大學生活多姿多彩"
    sentence3 = "有冇諗過冇人想知"
    sentence4 = "廣東話容唔容易學"
    sentence5 = "大家都好中意食麥當勞"
    sentence6 = "我老闆想我今晚十點之前做完啲嘢"
    # Forward case. It should output "中國/嘅/伊斯蘭/教會" instead of "中國/嘅/伊斯蘭教/會".
    sentence7 = "中國嘅伊斯蘭教會"
    # Backward case. It should output "/我/係/大學生/幹事/會/嘅/成員" instead of "/我/係/大學/生/幹事/會/嘅/成員".
    sentence8 = "我係大學生幹事會嘅成員"
    sentence9 = "聯合摺埋過檔新亞"
    sentence10 = "我係一個西伯利亞人"
    sentence11 = "大學生活多姿多彩"

    ### Sentence would like to analysis ###
    sentence = sentence11
    sentence = []
    sentence.append(sentence1)
    sentence.append(sentence2)
    sentence.append(sentence3)
    sentence.append(sentence4)
    sentence.append(sentence5)
    sentence.append(sentence6)

    final_sentence_list = seperate(sentence)
    print(final_sentence_list)

    #final_sentence_list = ['世一/中場/佐/真/奴', '大學/生活/多姿/多彩', '有冇/諗過/冇人/想/知', '廣東/話/容/唔/容易/學', '大家/都/好/中意/食/麥當勞', '我/老闆/想/我/今晚/十點/之前/做完/啲/嘢']
    correct_sentence_list = ['世一/中場/佐真奴', '大學/生活/多姿多彩', '有冇/諗過/冇人/想/知', '廣東話/容/唔/容易/學', '大家/都/好/中意/食/麥當勞', '我/老闆/想/我/今晚/十點/之前/做完/啲/嘢']

    #Calculate Precision
    f_score(final_sentence_list, correct_sentence_list)


