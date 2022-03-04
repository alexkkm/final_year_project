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

def extract_pos(filename):
    result_list = read_data(filename)
    return result_list

def extract_all_pos():
    result = extract_pos("pos_data/FC-001_v2")
    result = result+extract_pos("pos_data/FC-005a_v2")
    result = result+extract_pos("pos_data/FC-005b_v2")
    result = result+extract_pos("pos_data/FC-009b_v")
    result = result+extract_pos("pos_data/FC-011_v")
    result = result+extract_pos("pos_data/FC-012_v")
    result = result+extract_pos("pos_data/FC-013_v")
    result = result+extract_pos("pos_data/FC-018_v")
    result = result+extract_pos("pos_data/FC-019_v")
    result = result+extract_pos("pos_data/FC-020_v")
    result = result+extract_pos("pos_data/FC-022a_v")
    result = result+extract_pos("pos_data/FC-022b_v")
    result = result+extract_pos("pos_data/FC-026_v2")
    result = result+extract_pos("pos_data/FC-027_v2")
    result = result+extract_pos("pos_data/FC-028_v2")
    result = result+extract_pos("pos_data/FC-029_v")
    result = result+extract_pos("pos_data/FC-033_v2")
    result = result+extract_pos("pos_data/FC-035_v2")
    result = result+extract_pos("pos_data/FC-038a_v2")
    result = result+extract_pos("pos_data/FC-038b_v2")
    result = result+extract_pos("pos_data/FC-042_v")
    result = result+extract_pos("pos_data/FC-044_v2")
    result = result+extract_pos("pos_data/FC-045_v2")
    result = result+extract_pos("pos_data/FC-046_v2")
    result = result+extract_pos("pos_data/FC-048_v2")
    result = result+extract_pos("pos_data/FC-049_v2")
    result = result+extract_pos("pos_data/FC-052_v2")
    result = result+extract_pos("pos_data/FC-053_v2")
    result = result+extract_pos("pos_data/FC-055_v2")
    result = result+extract_pos("pos_data/FC-056_v2")
    result = result+extract_pos("pos_data/FC-101_v2")
    result = result+extract_pos("pos_data/FC-103_v2")
    result = result+extract_pos("pos_data/FC-104_v2")
    result = result+extract_pos("pos_data/FC-105_v2")
    result = result+extract_pos("pos_data/FC-106a_v2")
    result = result+extract_pos("pos_data/FC-106b_v2")
    result = result+extract_pos("pos_data/FC-107_v2")
    result = result+extract_pos("pos_data/FC-108a_v2")
    result = result+extract_pos("pos_data/FC-108c_v2")
    result = result+extract_pos("pos_data/FC-108d_v2")
    result = result+extract_pos("pos_data/FC-109a_v2")
    result = result+extract_pos("pos_data/FC-R002a_v2")
    result = result+extract_pos("pos_data/FC-R002b_v2")
    result = result+extract_pos("pos_data/FC-R003_v2")
    result = result+extract_pos("pos_data/FC-R004_v2")
    result = result+extract_pos("pos_data/FC-R005_v2")
    result = result+extract_pos("pos_data/FC-R006_v2")
    result = result+extract_pos("pos_data/FC-R007_v2")
    result = result+extract_pos("pos_data/FC-R009_v")
    result = result+extract_pos("pos_data/FC-R010a_v")
    result = result+extract_pos("pos_data/FC-R010b_v")
    result = result+extract_pos("pos_data/FC-R011_v")
    result = result+extract_pos("pos_data/FC-R013a_v")
    result = result+extract_pos("pos_data/FC-R013b_v")
    result = result+extract_pos("pos_data/FC-R016_v")
    result = result+extract_pos("pos_data/FC-R017_v")
    result = result+extract_pos("pos_data/FC-R018_v")
    return result

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

def extract_all_label():
    print("yes")
    fp = open("labeled_data/labeled_data.txt", "w+", encoding='utf-8')
    result = extract_all()
    for label_data in result:
        if label_data != "" and len(label_data.replace(" ", "")) > 2:
            s = label_data.replace(" ", "/")
            fp.write(s.replace("//", "/").replace("///", "/").replace("////", "/").replace("/////", "/") + "\n")
    fp.close()

def label_to_seperate_data():
    fp = open("testing_data/testing_data.txt", "w+", encoding='utf-8')
    fq = open("testing_data/correct_data.txt", "w+", encoding='utf-8')
    with open("testing_data/test.txt", 'r+', encoding='utf-8') as fd:
        sentence_list = fd.readlines()

    for sentence in sentence_list:
        s = sentence.replace("\n", "").split("\t")
        new_sentence = ""
        count = 0
        for c in s[1]:
            if c == 's' or c == 'e':
                new_sentence = new_sentence + s[0][count] + '/'
                count += 1
            else:
                new_sentence += s[0][count]
                count += 1
        fp.write(s[0] + "\n")
        fq.write(new_sentence + "\n")
        
def to_pos_data():
    fp = open("pos_data/dev.txt", "w+", encoding='utf-8')
    #with open("pos_data/FC-013_v", 'r+', encoding='utf-8') as fd:
    #    sentence_list = fd.readlines()
    sentence_list = extract_all_pos()
    all_sentence = ''
    for sentence in sentence_list:
        if '>' not in sentence:
            all_sentence+=sentence.replace('\n','').replace('	', '')
    all_sen = all_sentence.split("INFO-ENDA:")
    all_sen2 = ''
    for y in range(len(all_sen)):
        if y % 2 == 1:
            all_sen2+=all_sen[y]
    fp.write(all_sen2)

def to_pos_data2():
    fp = open("pos_data/dev3.txt", "w+", encoding='utf-8')
    with open("pos_data/dev.txt", 'r+', encoding='utf-8') as fd:
        sentence = fd.readlines()
    new_sentence=''
    for s in sentence:
        new_sentence = s.replace("A:", "").replace("B:", "").replace("C:", "").replace("D:", "").replace("S:", "").replace("J:", "").replace("M:", "").split("/")
    all_sentence=''
    for x in range(len(new_sentence)):
        if x % 3 != 2:
            if x % 3 == 0:
                new_sentence2=new_sentence[x]+"/"
                all_sentence+=new_sentence2
            elif x % 3 == 1:
                if new_sentence[x-1] != "。":
                    new_sentence2=new_sentence[x]+"  "
                    all_sentence+=new_sentence2
                else:
                    new_sentence2=new_sentence[x]+"  "+"\n"
                    all_sentence+=new_sentence2
    fp.write(all_sentence[:-1])

def to_pos_data3():
    fp = open("pos_data/train2.txt", "w+", encoding='utf-8')
    with open("pos_data/train.txt", 'r+', encoding='utf-8') as fd:
        sentence_list = fd.readlines()
    for x in sentence_list:
        y=x.replace("y1", "y").replace("v1", "v").replace("l1", "l").replace("g1", "g").replace("d1", "d")
        fp.write(y)

def to_label_data():
    fp = open("labeled_data/labeled_data2.txt", "w+", encoding='utf-8')
    with open("labeled_data/labeled_data.txt", 'r+', encoding='utf-8') as fd:
        sentence_list = fd.readlines()
    
    for sentence in sentence_list:
        label = ""
        s = sentence.replace("\n", "").split("/")
        for i in s:
            if len(i) == 1:
                label += 's'
            elif len(i) == 2:
                label += 'be'
            elif len(i) > 2:
                label += 'b'
                for j in range(len(i) - 2):
                    label += 'm'
                label += 'e'
        fp.write(sentence.replace("\n", "").replace("/", "") + "\t" + label + "\n")
#  Implementation: Extract the labelled data from FC-001_v2.cha

def removeDups():
    infilename = 'labels.txt'
    outfilename = 'labels2.txt'
    lines=open(infilename, 'r+', encoding='utf-8').readlines()
    lines_set = set(lines)
    out=open(outfilename, 'w+', encoding='utf-8')
    for line in lines_set:
        out.write(line)

def extract_label():
    fp = open("labels.txt", "w+", encoding='utf-8')
    with open("train.txt", 'r+', encoding='utf-8') as fd:
        sentence_list = fd.readlines()
    sentence = []
    sentence2 = []
    #sentence_list = ["喂/e  遲/a  啲/u  去/v  唔/d  去/v  旅行/vn  啊/y  ？/w  你/r  老公/n  有冇/v  平/a  機票/n  啊/y  ？/w  平/a  機票/n  要/vu  淡季/an  先/d  有得/vu  平/a  𡃉/y  喎/y  。/w  "]
    for x in sentence_list:
        sentence = x.split("  ")
        sentence = sentence[:-1]
        for y in sentence:
            sentence2 = y.split("/")
            fp.write(sentence2[1]+"\n")

if __name__ == '__main__':
    #extract_all_label()
    #label_to_seperate_data()
    #removeDups()
    #to_pos_data()
    #to_pos_data2()
    #to_pos_data3()
    #extract_label()
    removeDups()
    #print(extract("labeled_data/FC-001_v2.cha"))