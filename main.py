# Import the PrefixTree from prefixTree.py
from prefixTree import PrefixTree

# Convert the multi-lines of strings into list
def string_to_list(string):
    list_string = list(string.split("\n"))
    return list_string   


############## Implementation (Main Function) ####################
if __name__ == '__main__':

    # Create a file pointer fd, open the vocab_dictionart.txt with read-only mode
    fd = open("vocab_dictionary.txt", "r", encoding="utf-8")
    str = fd.read()
    dict_list = string_to_list(str)

    # Build a PrefixTree called trie
    trie = PrefixTree()

    # For all vocabs in dictionary list:
    for string in dict_list:
        # Insert the words into the PrefixTree trie
        trie.insert(string)

    # Real Implementation: Print out all vocabs starts with '專'
    print(trie.starts_with('專'))
