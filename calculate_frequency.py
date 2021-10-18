from DictionaryPrefixTree import DictionaryPrefixTree
from extract import extract_all


def calculating_frequency():
    with open("dictionary/vocab_dictionary.txt", 'r', encoding='utf-8') as fd:
        dictionary_list = fd.readlines()
    # Remove space appears in all lines of dictionary_list
    dictionary_list = [line.rstrip() for line in dictionary_list]

    dictionary_dict = dict.fromkeys(dictionary_list, 0)

    label_data = extract_all()
    dictionary = {}

    progress = 0

    # For each substring, count the number of occurrences in label data.
    for vocab in dictionary_dict:
        for y in label_data:
            count_char = 0
            count_char += y.count(vocab)
        dictionary[vocab] = count_char
        progress += 1
        print("Progress:")
        print(progress)

    # Write the result into new file
    with open("vocab_frequency_in_label_data.txt", "w+", encoding='utf-8') as fp:
        fp.write("freqency:\n")
        fp.write(str(dictionary))


if __name__ == '__main__':
    print("end")
