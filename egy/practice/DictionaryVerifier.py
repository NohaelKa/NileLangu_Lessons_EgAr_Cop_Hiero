# -*- coding: utf-8 -*-
import os
from typing import Dict

def isEnglish(s):
    try:
        s.encode(encoding='utf-8').decode('ascii')
    except UnicodeDecodeError:
        return False
    else:
        return True

def doesAudioExist(my_list):
    ret = 0
    print("audio that needs recording")
    for string in my_list:
        if not os.path.exists("../audio/"+string+".m4a"):
            print(string)
            ret = 1

    return ret
            
def wordsInExercise(my_list):
    print(my_list)

def read_file(num):
    my_list = []
    file = open('lesson_'+str(num)+'.txt', encoding="utf8")
    lines = file.readlines() # list containing lines of file
    file.close()

    for line in lines:
        line = line.strip() # remove leading/trailing white spaces
        if line:
            data = line.split(',')
            for word in data:
                if not isEnglish(word) and not(' ' in word) and not(':' in word) and not len(word)==1:
                    my_list.append(word) # append dictionary to list

    my_list = list(dict.fromkeys(my_list))
    return my_list

def read_Dictionary(num):
    my_list = []
    file = open('lesson_'+str(num)+'.txt', encoding="utf8")
    lines = file.readlines() # list containing lines of file
    file.close()
    startDict = False
    for line in lines:
        line = line.strip() # remove leading/trailing white spaces
        if str(line) == "-":
            startDict = False
        if startDict:
            my_list.append(line.split(':'))   
        if str(line) == "Dictionary":
            startDict = True
        
    return my_list

def Convert(lst):
    res_dct = {lst[i][1]: lst[i][0] for i in range(0, len(lst))}
    return res_dct


def main():
    num = 1
    my_list = []
    full_Dict_list = []
    while (num != 30):
        print(num)

        my_list = read_file(num)
        Dict_list = read_Dictionary(num)
        for a in Dict_list:
            full_Dict_list.append(a)
        num+=1
        Dic = Convert(Dict_list)
        for word in my_list:
            if word in Dic.keys():
                pass
            else:
                #print(word)
                pass

    print(len(full_Dict_list))
    #for a in full_Dict_list:
    #    print(a)
    Full_Dic = Convert(full_Dict_list)
    print(len(Full_Dic))
    
    print("error")
    num = 1
    not_in_list = list()

    while (num != 30):
        print(num)

        my_list = read_file(num)
        Dict_list = read_Dictionary(num)
        num+=1
        Dic = Convert(Dict_list)
        for word in my_list:
            if word in Dic.keys():
                pass
            else:
                if word in Full_Dic.keys():
                    print(Full_Dic[word] + ":"+ word )
                
                else:    
                    print("[] test:" + word)
                    not_in_list.append(word)
                    
    print(len(not_in_list))
    not_in_list = list(dict.fromkeys(not_in_list))
    print(not_in_list)
    print(len(not_in_list))

    #print(Dic)
    #while (num != 30):
    #   my_list = read_file(num)
    #   ret = doesAudioExist(my_list)
    #   if ret == 1:
    #        break
    #   num+=1


main()
