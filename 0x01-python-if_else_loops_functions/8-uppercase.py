#!/usr/bin/python3
def uppercase(str):

    str1 = ""
    for i in str:
        if ord(i) >= 97 and ord(i) < 123:
            #'chr' is used to find the character from ASCII value
            str1 += chr(ord(i) - 32)
        else:
            str1 += i
    print("{}".format(str1))
