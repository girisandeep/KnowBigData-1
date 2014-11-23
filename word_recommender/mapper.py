#!/usr/bin/python

#Get each line from the file. Remove all special characters, tabs, multpile white spaces to 
#a single one and new line characters.
#Split the line by space and get all words.
#Print the words in key value pairs such that 1st word is a key and the 2nd word is a value.
#Similarly the 2nd word is a key to the 3rd word, a value. So on and so forth.

import sys
import re

#Regular expression to match any non-alphanumberic character
pattern = re.compile("\W+")

for line in sys.stdin:
    line = line.strip()
    line = re.sub("[^a-zA-Z0-9_ ]", "", line)

    data = line.split(" ")

    i = 0
    previous = ""

    for word in data:
        if i == 1 and previous != "":
                print "{0}\t{1}".format(previous, word)
                previous = word
                continue
        i += 1
        previous = word

