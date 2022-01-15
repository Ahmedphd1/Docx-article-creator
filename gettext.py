import requests
from processtext import *
from random import randrange
from docx import Document

def dividebytext(text):
    listoftext = []

    strippedtext = str(text).strip()

    textcount = int(int(len(strippedtext) - 1) / 30)

    print(textcount)

    startindex = 0
    endindex = textcount

    print("Starting to divide text into pages")

    for x in range(11):
        if endindex < len(strippedtext) - 1:
            listoftext.append(strippedtext[startindex:endindex])

            startindex = endindex
            endindex += textcount
        else:
            listoftext[-1] += strippedtext[startindex:endindex]
            return listoftext

    print("All pages created")
    return listoftext
















