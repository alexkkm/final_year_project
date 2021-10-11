# Structure of Dictionary Prefix Tree

# TrieNode: null char is added into the text when init, and contains a dict for storing all its children
class TrieNode:
    def __init__(self, text=''):
        self.text = text
        self.children = dict()
        ''' dict={character of the child: address of the child Trienode} '''
        self.is_word = False
        '''Boolean indicating if the words together in front of the TrieNode is a single word'''


# Prefix Tree is built with a root node which is a null node when init
class DictionaryPrefixTree:

    def __init__(self):
        self.root = TrieNode()

    # Operations of Prefix Tree

    # Inserting a new word to a DictionaryPrefixTree
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

    # Private helper function. Cycles through all children of node recursionly, adding them to words if they constitute whole words
    def __child_words_for(self, node, words):
        if node.is_word:
            words.append(node.text)
        for letter in node.children:
            self.__child_words_for(node.children[letter], words)

    # Recursion function for looking for the vocab within the dictionary in the sentence
    def recursion(self, sentence, dictionary):
        word = ''
        current = self.root
        if len(sentence) > 0:
            for idx, letter in enumerate(sentence):
                if letter not in current.children:
                    current = self.root

                if letter in current.children:
                    current = current.children[letter]
                    word += letter
                    # print('progress:', word)
                    if current.is_word:
                        if current.text not in dictionary:
                            dictionary.append(current.text)
                            # print('found:', current.text)
                        self.recursion(sentence[idx+1:], dictionary)
        if len(word) == len(sentence):
            return dictionary
    # Return a list of vocab which is contains in the given sentence

    def contains(self, sentence):
        dictionary = list()
        return self.recursion(sentence, dictionary)

    # Main Dishes: Returning the segmented sentence  // Not implement yet
    def segment(self, prefix):
        the_word = ""
        current = self.root
        for char in prefix:
            if char not in current.children:
                the_word = the_word + " / "
                current = self.root
            current = current.children[char]
            the_word = the_word + char
        return the_word


##### Example (Example: Print out all substring of the sentence which appears in the dictionary) #####
if __name__ == '__main__':

    # Build a DictionaryPrefixTree called trie
    trie = DictionaryPrefixTree()

    # Create a file pointer fd,open th vocab_dictionary with read-only mode
    with open("dictionary/vocab_dictionary.txt", 'r', encoding='utf-8') as fd:
        dictionary_list = fd.readlines()
        # Remove space appears in all lines of dictionary_list
        dictionary_list = [line.rstrip() for line in dictionary_list]

    # For all vocabs in dictionary_list
    for vocabs in dictionary_list:
        # Insert the words into the DictionaryPrefixTree trie
        trie.insert(vocabs)

    # Print out all vocabs of the sentence which appears in the dictionary
    sentence = "中國伊斯蘭教會"
    sentence2 = "大家一齊去食麥當勞"

    # Print all vocabs contains in sentence
    print(trie.contains(sentence))

    # Old methods to do contains function
    dictionary = list()
    print(trie.recursion(sentence2, dictionary))
