#!/usr/bin/python

import sys

oldKey = None
anagrams = []

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

    thisKey, thisWord = data_mapped

    if oldKey and oldKey != thisKey:
        if len(anagrams) > 1:
		anagrams.sort()
		print anagrams

        anagrams = []

    oldKey = thisKey
    anagrams.append(thisWord)

if oldKey != None:
    if len(anagrams) > 1:
		anagrams.sort()
                print anagrams

