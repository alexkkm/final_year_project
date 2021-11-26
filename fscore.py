
# Output the calculation of Precision,Recall,F-score by given output sentence list and given correct sentence list
def f_score(segmentation_result, correct_sentence_list):
    number_of_sentence = len(segmentation_result)

    # initialize the sentence in given sentence_list
    # Calculate the Precision, Recall and F-score of the System
    precision = 0
    recall = 0
    for k in range(number_of_sentence):
        count_TP = 0
        count_FP = 0
        count_FN = 0
        sentence1 = segmentation_result[k]
        sentence2 = correct_sentence_list[k]
        s1 = sentence1.split("/")
        s2 = sentence2.split("/")
        count_FP = len(s1)
        count_FN = len(s2)
        count_TP = len(set(s1) & set(s2))
        precision += count_TP / count_FP
        recall += count_TP / count_FN
        #print("TP:", count_TP)
        #print("FP:", count_FP)
        #print("FN:", count_FN)

    precision = precision / number_of_sentence
    recall = recall / number_of_sentence
    f_score = (2 * precision * recall)/(precision + recall)

    # Print the calulated Precision, Recall and F-score of System
    print("Scoring Result: ")
    print("Precision:", precision)
    print("Recall:", recall)
    print("F-score:", f_score)

    return f_score
