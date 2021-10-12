# Extract the sentence in label dataset, and print it in a single document


# Read the target label dataset file
def read_data(filename):
    # Create a file pointer fd,open th vocab_dictionary with read-only mode
    with open(filename, 'r', encoding='utf-8') as fd:
        sentence_list = fd.readlines()
    return sentence_list


# filter out all sentences in given sentence_list without given keywords
def filter_by_keyword(sentence_list, keyword):
    filtered = [
        sentence for sentence in sentence_list if sentence.startswith(keyword)]
    return filtered


# Remove all symbol made in labelled dataset
def remove_symbol(filtered):

    # defining special characters and English characters
    special_char = '@_-!#$%^&*()<>?/\|}{~:;.,[]\n\t'
    english_char = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    all_char = special_char+english_char

    # filtered all unused character appeared in above sets
    result = [''.join(filter(lambda i: i not in all_char, string))
              for string in filtered]
    return result

# Implementation: Extract the labelled data from FC-001_v2.cha
def extract():
    result_list = read_data("labeled_data/FC-001_v2.cha")
    filter_result = filter_by_keyword(result_list, "*")
    final = remove_symbol(filter_result)
    return final

'''
# Implementation: Extract the labelled data from FC-001_v2.cha
if __name__ == '__main__':
    result_list = read_data("labeled_data/FC-001_v2.cha")
    filter_result = filter_by_keyword(result_list, "*")
    final = remove_symbol(filter_result)
    print(final)
'''
