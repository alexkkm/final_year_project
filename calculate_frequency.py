from DictionaryPrefixTree import DictionaryPrefixTree
from extract import extract_all


if __name__ == '__main__':
    with open("dictionary/vocab_dictionary.txt", 'r', encoding='utf-8') as fd:
        dictionary_list = fd.readlines()
    # Remove space appears in all lines of dictionary_list
    dictionary_list = [line.rstrip() for line in dictionary_list]

    dictionary_dict = dict.fromkeys(dictionary_list, 0)

    label_data = extract_all()
    dictionary = {}
    count_char = 0
    counter = 0

    # For each substring, count the number of occurrences in label data.
    for vocab in dictionary_dict:
        for y in label_data:
            count_char += y.count(vocab)
        dictionary[vocab] = count_char
        counter += 1
        print("counter:")
        print(counter)

    fp = open("vocab_frequency_in_label_data.txt", "w+", encoding='utf-8')
    fp.write("frqency:\n")
    fp.write(dictionary_dict)
