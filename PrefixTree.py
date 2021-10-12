from extract import extract
from DictionaryPrefixTree import DictionaryPrefixTree
# Structure of Prefix Tree

# TrieNode: null char is added into the text when init, and contains a dict for storing all its children
class TrieNode:
    def __init__(self, text=''):
        self.text = text
        # dict={character of the child: address of the child Trienode}
        self.children = dict()
        # A Boolean indicating if the words together in front of the TrieNode is a single word
        self.is_word = False


# Prefix Tree is built with a root node which is a null node when init
class SentencePrefixTree:

    def __init__(self):
        self.root = TrieNode()

# Operations of Prefix Tree:
    # Inserting a new word to a SentencePrefixTree
    def insert(self, word):
        current = self.root
        for i, char in enumerate(word):
            if char not in current.children:
                prefix = word[0:i+1]
                current.children[char] = TrieNode(prefix)
            current = current.children[char]
        current.is_word = True

    # Returning the TrieNode representing the given word
    def find(self, word):
        '''
        Returns the TrieNode representing the given word if it exists
        and None otherwise.
        '''
        current = self.root
        for char in word:
            if char not in current.children:
                return None
            current = current.children[char]

        if current.is_word:
            return current

    # Returning a list of all words beginning with the given prefix, or an empty list if no words begin with that prefix
    def starts_with(self, prefix):
        words = list()
        current = self.root
        for char in prefix:
            if char not in current.children:  # if that prefix are not appeared in the Tree, return empty list
                return list()
            current = current.children[char]

        self.__child_words_for(current, words)
        return words

    # Private helper function. Cycles through all children of node recursively, adding them to words if they constitute whole words
    def __child_words_for(self, node, words):
        if node.is_word:
            words.append(node.text)
        for letter in node.children:
            self.__child_words_for(node.children[letter], words)

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


### Example (Simple Example of Prefix Tree)  ###
if __name__ == '__main__':

    # Build a SentencePrefixTree called trie
    trie = SentencePrefixTree()

    sentance = "我係一個西伯利亞人"

    # Insert the words into the SentencePrefixTree trie
    trie.insert('我係一個西伯利亞人')
    #trie.insert('今天我寒夜裡看雪飄過')
    #trie.insert('世一中場佐真奴')

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

    print(dict_trie.contains(sentance))

    # Separate the sentance and search it from the label data
    sentance_list = trie.seperate(sentance)
    label_data = extract()
    label_data_len = len(label_data)
    dict = {}
    count_char = 0
    # For each substring, count the number of occurrences in label data.
    for x in sentance_list:
        for y in label_data:
            count_char += y.count(x)
        dict[x] = count_char
        count_char = 0

    print(dict)
    # print(len(label_data))

    # Print out all sentences start with '我'
    # print(trie.starts_with('我'))