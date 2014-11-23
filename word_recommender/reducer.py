#!/usr/bin/python

import sys

oldKey = None
suggestions = {}

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
        suggestions = sorted(suggestions, key=suggestions.__getitem__, reverse=True)
        print oldKey, "\t", suggestions
        suggestions = {}

    oldKey = thisKey
    if str(thisWord) not in suggestions:
        suggestions[str(thisWord)] = int(1)
    else:
        count = suggestions[str(thisWord)]
        count += 1
        suggestions[str(thisWord)] = int(count)

if oldKey != None:
    suggestions = sorted(suggestions, key=suggestions.__getitem__, reverse=True)
    print oldKey, "\t", suggestions
    suggestions = {}
