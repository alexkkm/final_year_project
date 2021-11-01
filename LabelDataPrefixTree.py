from extract import extract_all
# Structure of Label Data Prefix Tree

# TrieNode: null char is added into the text when init, and contains a dict for storing all its children
class TrieNode:
    def __init__(self, text=''):
        self.text = text
        self.children = dict()
        ''' dict={character of the child: address of the child Trienode} '''
        self.is_word = False
        '''Boolean indicating if the words together in front of the TrieNode is a single word'''


# Prefix Tree is built with a root node which is a null node when init
class LabelDataPrefixTree:

    def __init__(self):
        self.root = TrieNode()
        self.dictionary = {}

# Operations of Prefix Tree
    # Inserting a new word to a LabelDataPrefixTree
    def insert(self, word):
        current = self.root
        for i in range(len(word)):
            for j in range(1,len(word)+1):
                if j > i:
                    if word[i:j] not in self.dictionary:
                        self.dictionary[word[i:j]] = 0
                    self.dictionary[word[i:j]] += 1

        for i, char in enumerate(word):
            if char not in current.children:
                prefix = word[0:i+1]
                current.children[char] = TrieNode(prefix)
            current = current.children[char]
        current.is_word = True

    def get_frequency(self, word):
        count = 0
        if word in self.dictionary:
            count = self.dictionary[word]
        else:
            count = 0
        return count

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

    # Build a LabelDataPrefixTree called trie
    trie = LabelDataPrefixTree()

    label_data = extract_all()
    for label_data_list in label_data:
        label_data_split = label_data_list.split()
        # For all vocabs in label_data_list
        for vocabs in label_data_split:
            # Insert the words into the LabelDataPrefixTree trie
            trie.insert(vocabs)

    # Print out all vocabs of the sentence which appears in the dictionary
    sentence = "中國伊斯蘭教會"
    sentence2 = "大家一齊去食麥當勞"
    sentence3 = "嗰陣時去"
    # Print all vocabs contains in sentence
    print(trie.contains(sentence))
    print(trie.get_frequency("嗰陣"))
    print(trie.get_frequency("時"))
    print(trie.get_frequency("嗰陣時"))
    print(trie.get_frequency("大學生"))
    print(trie.get_frequency("大學"))
    print(trie.get_frequency("生"))
    # Old methods to do contains function
    #dictionary = list()
    #print(trie.recursion(sentence2, dictionary))
