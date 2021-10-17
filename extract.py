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


# Main function: Extract the labelled data from target file
def extract(filename):
    # Read the target label dataset file
    result_list = read_data(filename)
    # filter out all sentences in target file without '*'
    filter_result = filter_by_keyword(result_list, "*")
    # Remove all symbol made in labelled dataset
    final_result = remove_symbol(filter_result)
    # Return the final result
    return final_result


# Extract all label dataset from all file in label_data
def extract_all():

    result = extract("labeled_data/FC-001_v2.cha")
    result = result+extract("labeled_data/FC-005a_v2.cha")
    result = result+extract("labeled_data/FC-005b_v2.cha")
    result = result+extract("labeled_data/FC-009b_v.cha")
    result = result+extract("labeled_data/FC-011_v.cha")
    result = result+extract("labeled_data/FC-012_v.cha")
    result = result+extract("labeled_data/FC-013_v.cha")
    result = result+extract("labeled_data/FC-018_v.cha")
    result = result+extract("labeled_data/FC-019_v.cha")
    result = result+extract("labeled_data/FC-020_v.cha")
    result = result+extract("labeled_data/FC-022a_v.cha")
    result = result+extract("labeled_data/FC-022b_v.cha")
    result = result+extract("labeled_data/FC-026_v2.cha")
    result = result+extract("labeled_data/FC-027_v2.cha")
    result = result+extract("labeled_data/FC-028_v2.cha")
    result = result+extract("labeled_data/FC-029_v.cha")
    result = result+extract("labeled_data/FC-033_v2.cha")
    result = result+extract("labeled_data/FC-035_v2.cha")
    result = result+extract("labeled_data/FC-038a_v2.cha")
    result = result+extract("labeled_data/FC-038b_v2.cha")
    result = result+extract("labeled_data/FC-042_v.cha")
    result = result+extract("labeled_data/FC-044_v2.cha")
    result = result+extract("labeled_data/FC-045_v2.cha")
    result = result+extract("labeled_data/FC-046_v2.cha")
    result = result+extract("labeled_data/FC-048_v2.cha")
    result = result+extract("labeled_data/FC-049_v2.cha")
    result = result+extract("labeled_data/FC-052_v2.cha")
    result = result+extract("labeled_data/FC-053_v2.cha")
    result = result+extract("labeled_data/FC-055_v2.cha")
    result = result+extract("labeled_data/FC-056_v2.cha")
    result = result+extract("labeled_data/FC-101_v2.cha")
    result = result+extract("labeled_data/FC-103_v2.cha")
    result = result+extract("labeled_data/FC-104_v2.cha")
    result = result+extract("labeled_data/FC-105_v2.cha")
    result = result+extract("labeled_data/FC-106a_v2.cha")
    result = result+extract("labeled_data/FC-106b_v2.cha")
    result = result+extract("labeled_data/FC-107_v2.cha")
    result = result+extract("labeled_data/FC-108a_v2.cha")
    result = result+extract("labeled_data/FC-108c_v2.cha")
    result = result+extract("labeled_data/FC-108d_v2.cha")
    result = result+extract("labeled_data/FC-109a_v2.cha")
    result = result+extract("labeled_data/FC-R002a_v2.cha")
    result = result+extract("labeled_data/FC-R002b_v2.cha")
    result = result+extract("labeled_data/FC-R003_v2.cha")
    result = result+extract("labeled_data/FC-R004_v2.cha")
    result = result+extract("labeled_data/FC-R005_v2.cha")
    result = result+extract("labeled_data/FC-R006_v2.cha")
    result = result+extract("labeled_data/FC-R007_v2.cha")
    result = result+extract("labeled_data/FC-R009_v.cha")
    result = result+extract("labeled_data/FC-R010a_v.cha")
    result = result+extract("labeled_data/FC-R010b_v.cha")
    result = result+extract("labeled_data/FC-R011_v.cha")
    result = result+extract("labeled_data/FC-R013a_v.cha")
    result = result+extract("labeled_data/FC-R013b_v.cha")
    result = result+extract("labeled_data/FC-R016_v.cha")
    result = result+extract("labeled_data/FC-R017_v.cha")
    result = result+extract("labeled_data/FC-R018_v.cha")

    return result


#  Implementation: Extract the labelled data from FC-001_v2.cha
if __name__ == '__main__':
    result = extract_all()
    print(result)