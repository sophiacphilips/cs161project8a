#Author: Sophia Philips
#GitHub Username: sophiacphilips
#Date: 11/15/22
#This project takes a string of letters and returns a dictionary that lists the number of each letter in the string

def count_letters(letters_input):
    """this take a string of letters and return a dictionary listing the amount of each letter present"""
    d = {}
    for i in letters_input: #for the letters in the string
        i = i.upper()  #changes all letters to uppercase so they will all be counted
        if ("A" <= i <= "Z"):  #for all letters A through Z, if they are not in the string=0, if they are, lists the number of them present
            if i not in d:
                d[i]=0
            d[i]+=1
    return d


#print(count_letters("AaBb"))