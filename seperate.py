from extract import extract_all
from DictionaryPrefixTree import DictionaryPrefixTree
from PrefixTree import PrefixTree

# Seperate the sentance as a prefix tree structure and return a list.


def seperate(self, sentance):
    sentance_list = list()
    sentance_len = len(sentance)
    # We set the maximum number of character in a single word as 5.
    max_char = 5
    for i in range(sentance_len - max_char + 1):
        str1 = sentance[i:max_char+i]
        for j in range(1, max_char + 1):
            str2 = str1[0:j]
            str3 = str1[j:max_char]
            if str2 != "":
                sentance_list.append(str2)
            if str3 != "":
                sentance_list.append(str3)
    return sentance_list


### Example (print out frequency and vocabs of given sentence)  ###
if __name__ == '__main__':

    # Build a PrefixTree called trie
    trie = PrefixTree()

    # Sentence would like to analysis
    sentence = "廣東話容唔容易學"

    sentence1 = "世一中場佐真奴"
    sentence2 = "今天我寒夜裡看雪飄過"
    sentence3 = ""
    sentence4 = "我係一個西伯利亞人"

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
    print(dict_trie.contains(sentence))
    print("\n")
    # Separate the sentance and search it from the label data
    sentance_list = trie.seperate(sentence)
    label_data = extract_all()
    label_data_len = len(label_data)
    dict = {}
    count_char = 0
    # For each substring, count the number of occurrences in label data.
    for x in sentance_list:
        for y in label_data:
            count_char += y.count(x)
        dict[x] = count_char
        count_char = 0
    print("frequency:")
    print(dict)
