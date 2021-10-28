from fscore import f_score
from segment import segment


# Input a list of unsegmented sentence,
# output the segmentation result,calculating the F-score
# (Now unable the merging measure)

if __name__ == '__main__':

    sentence1 = "世一中場佐真奴"
    sentence2 = "大學生活多姿多彩"
    sentence3 = "你嗰陣時有冇諗過冇人想知" # Now is "嗰陣/時", we should change to "嗰陣時" by considering label data
    sentence4 = "廣東話容唔容易學"
    sentence5 = "大家都好中意食麥當勞"
    sentence6 = "我老闆想我今晚十點之前做完啲嘢"
    # Forward case. It should output "中國/嘅/伊斯蘭/教會" instead of "中國/嘅/伊斯蘭教/會".
    sentence7 = "中國伊斯蘭教嘅伊斯蘭教會"
    # Backward case. It should output "/我/係/大學生/幹事/會/嘅/成員" instead of "/我/係/大學/生/幹事/會/嘅/成員".
    sentence8 = "我係大學生幹事會嘅成員"
    sentence9 = "聯合摺埋過檔新亞"
    sentence10 = "我係一個西伯利亞人"
    sentence11 = "大學生活多姿多彩"

    ### Sentence would like to analysis ###
    sentence = sentence11
    sentence_list = []
    #sentence_list.append(sentence1)
    #sentence_list.append(sentence2)
    #sentence_list.append(sentence3)
    #sentence_list.append(sentence4)
    #sentence_list.append(sentence5)
    #sentence_list.append(sentence6)
    sentence_list.append(sentence7)
    #sentence_list.append(sentence8)


    segmentation_result = segment(sentence_list)

    # Print the segmentation result
    print("\n")
    print("segmentation_result_list: "+str(segmentation_result))
    print("\n")

    '''
    correct_sentence_list = [
        '世一/中場/佐真奴',
        '大學/生活/多姿多彩',
        '你/嗰陣時/有冇/諗過/冇人/想/知',
        '廣東話/容/唔/容易/學',
        '大家/都/好/中意/食/麥當勞',
        '我/老闆/想/我/今晚/十點/之前/做完/啲/嘢']
    '''

    correct_sentence_list = [
        '你/嗰陣時/有冇/諗過/冇人/想/知', 
        '中國/伊斯蘭教/嘅/伊斯蘭/教會',
        '我/係/大學生/幹事會/嘅/成員']

    # Calculate Precision
    f_score(segmentation_result, correct_sentence_list)
