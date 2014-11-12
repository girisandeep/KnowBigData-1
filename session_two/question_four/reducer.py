#!/usr/bin/python

import sys

oldKey = None
dict = {}

# Loop around the data
# It will be in the format key\tval
# Where key is the word in sorted character order, val is the actual word
#
# Print all the words whose keys are equal and they are the anagrams

for line in sys.stdin:
    data_mapped = line.strip().split("\t")
    if len(data_mapped) != 2:
        # Something has gone wrong. Skip this line.
        continue

    thisKey, thisUser = data_mapped
    #Reverse the key using STRING[::-1]
    reverseKey = thisKey[::-1]
    
    if thisKey in dict:
	value = dict[thisKey] + ", " + thisUser
	dict[thisKey] = value
    elif reverseKey in dict:
	value = dict[reverseKey] + ", " + thisUser
	dict[reverseKey] = value
    else:
	dict[thisKey] = thisUser

keylist = dict.keys()
keylist.sort()

for key in keylist:
    print dict[key]
