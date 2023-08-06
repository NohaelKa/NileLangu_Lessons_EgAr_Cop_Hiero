# -*- coding: utf-8 -*-
import os

def isEnglish(s):
    try:
        s.encode(encoding='utf-8').decode('ascii')
    except UnicodeDecodeError:
        return False
    else:
        return True

def doesAudioExist(my_list):
    ret = 0
    for string in my_list:
        if not os.path.exists("C://Users//Nohae//OneDrive//Documents//ChatNao//NileLangu//NileLangu//src//main//assets//lang//egy//audio//"+string+".m4a"):
            print("audio that needs recording")
            print(string)
            ret = 1

    return ret
            
def wordsInExercise(my_list):
    print(my_list)

def read_file(num):
    my_list = []
    print(num)
    file = open('lesson_'+str(num)+'.txt', encoding="utf8")
    lines = file.readlines() # list containing lines of file
    file.close()

    for line in lines:
        line = line.strip() # remove leading/trailing white spaces
        if line:
            data = line.split(',')
            for word in data:
                if not isEnglish(word) and not(' ' in word) and not(':' in word):
                    my_list.append(word) # append dictionary to list

    my_list = list(dict.fromkeys(my_list))
    return my_list

def main():
    num = 1
    my_list = []

    while (num != 30):
        my_list = read_file(num)
        ret = doesAudioExist(my_list)
        num+=1


main()
