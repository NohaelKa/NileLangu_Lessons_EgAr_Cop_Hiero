# -*- coding: utf-8 -*-
import os
from typing import Dict

multichoice = 0
audiochoice = 0
imagechoice = 0
formsentence = 0
lessonNum = 0

def isEnglish(s):
    try:
        s.encode(encoding='utf-8').decode('ascii')
    except UnicodeDecodeError:
        return False
    else:
        return True

def doesBugExist(my_list):
    global multichoice
    global imagechoice
    for string in my_list:
##        ques = string[0]
##        ans = string[1:]
##        if string[0]== "multichoice":
##            multichoice = 1
##        elif multichoice == 1 and string[0] != "-":
##            #print(len(set(ans)))
##            if len(string) != 5:
##                print("Lesson Number: ", lessonNum)
##                print("actual length: ", len(string))
##                print("Num of ans error in multichoice" , string)
##                print("")
##            if len(ans) != len(set(ans)):
##                print("Lesson Number: ", lessonNum)
##                print("Duplicate ans error in multichoice" , string)
##                print("")
##        elif multichoice ==1 and string[0] == "-":
##            multichoice = 0
            
        if string[0]== "multichoice_img":
            imagechoice = 1
        elif imagechoice == 1:
            for word in string:
                if not os.path.exists("C://Users//Nohae//OneDrive//Documents//ChatNao//NileLangu//NileLangu//src//main//res//drawable//"+word+".png"):
                    print("Lesson Number: ", lessonNum)
                    print("Not existing image in imagechoice" , word)
                    print("")
            imagechoice = 0

          
def wordsInExercise(my_list):
    print(my_list)

def read_file(num):
    my_list = []
    file = open('lesson_'+str(num)+'.txt', encoding="utf8")
    #file = open("C://Users//Nohae//OneDrive//Documents//ChatNao//NileLangu//NileLangu//src//main//assets//lang//cop//practice//" + 'lesson_'+ str(num) +".txt", encoding='utf8')
    lines = file.readlines() # list containing lines of file
    file.close()

    for line in lines:
        line = line.strip() # remove leading/trailing white spaces
        if line:
            data = line.split(',')
            my_list.append(data) # append dictionary to list

    #my_list = list(dict.fromkeys(my_list))
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


def main():
    global lessonNum
    lessonNum = 1
    my_list = []
    while (lessonNum != 30):
       my_list = read_file(lessonNum)
       doesBugExist(my_list)
       lessonNum+=1


main()
