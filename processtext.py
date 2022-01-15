def removebooktitle(string, searchcriteriatop, searchcriteriabottom):
    print("Start processing function: Text")

    try:
        # remove top title
        wordindex = string.find(searchcriteriatop)

        newstring = string[0: 0:] + string[(wordindex - 1)::]

    except:
        print("Cant find top title: trying botton title")


    try:
        # remove bottom title
        wordindex = newstring.find(searchcriteriabottom)

        newstring = newstring[0: wordindex:] + newstring[len(newstring)::]

    except:
        print("Cant find bottom title")
        return None

    print("Finished processing text")
    return newstring

def changeauthor(string, searchcriteria, newauthor):

    try:
        newstring = string.replace(searchcriteria, newauthor)

        return newstring
    except:
        print("cant find author")

