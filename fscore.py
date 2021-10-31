
# Output the calculation of Precision,Recall,F-score by given output sentence list and given correct sentence list
def f_score(segmentation_result, correct_sentence_list):
    new_list1 = []
    new_list2 = []
    number_of_sentence = len(segmentation_result)

    # initialize the sentence in given sentence_list
    for sentence in segmentation_result:
        new_sentence = ""
        for i in range(len(sentence)-1):
            if sentence[i] != "/" and sentence[i+1] != "/":
                new_sentence += sentence[i] + "_"
            else:
                new_sentence += sentence[i]
        new_sentence += sentence[len(sentence)-1]
        new_list1.append(new_sentence)

    for correct_sentence in correct_sentence_list:
        new_sentence = ""
        for j in range(len(correct_sentence) - 1):
            if correct_sentence[j] != "/" and correct_sentence[j+1] != "/":
                new_sentence += correct_sentence[j] + "_"
            else:
                new_sentence += correct_sentence[j]
        new_sentence += correct_sentence[len(correct_sentence)-1]
        new_list2.append(new_sentence)

    # Calculate the Precision, Recall and F-score of the System
    precision = 0
    recall = 0
    for k in range(number_of_sentence):
        count_TP = 0
        count_FP = 0
        count_FN = 0
        sentence1 = new_list1[k]
        sentence2 = new_list2[k]
        for x in range(len(sentence1)):
            if sentence1[x] == "/" and sentence2[x] != "/":
                count_FP += 1  # FP
            if sentence1[x] == "/" and sentence2[x] == "/":
                count_TP += 1  # TP
            if sentence1[x] != "/" and sentence2[x] == "/":
                count_FN += 1  # FN
        precision += count_TP / (count_TP + count_FP)
        recall += count_TP / (count_TP + count_FN)
        #print("segmentation result: "+str(sentence1))
        #print("correct sentence: "+str(sentence2))
        #print("TP:", count_TP)
        #print("FP:", count_FP)
        #print("FN:", count_FN)
    precision = precision / number_of_sentence
    recall = recall / number_of_sentence
    f_score = (2 * precision * recall)/(precision + recall)

    #print("\n")

    # Print the calulated Precision, Recall and F-score of System
    print("Scoring Result: ")
    print("Precision:", precision)
    print("Recall:", recall)
    print("F-score:", f_score)
    return f_score
