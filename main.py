from gettext import *
from getimage import *
from createdocuments import *
from processtext import *


mytext = requests.get("http://www.gutenberg.org/files/74/74-0.txt").text.encode("ISO-8859-1").decode()

thetext = removebooktitle(mytext, "CONTENTS", "CONCLUSION")

wordlist = dividebytext(thetext)

imagelist = findimage(wordlist)

createdocument(wordlist, imagelist)

