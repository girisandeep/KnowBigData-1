#!/usr/bin/python

import sys
import re

oldKey = None
votes = {}
worth = {}
persons = {}
pattern = re.compile("[0-9]+")

# Loop around the data
# It will be in the format key\tval

for line in sys.stdin:
    data_mapped = line.strip().split("\t")
    if len(data_mapped) != 2:
        # Something has gone wrong. Skip this line.
        continue

    thisKey, thisValue = data_mapped
    
    if pattern.match(thisValue):
	worth[thisKey] = thisValue
	persons[thisKey] = int(0)
    else:
	votes[thisKey] = thisValue
	persons[thisValue] = int(0)
	persons[thisValue] = int(0)
	
for key in persons:
    worthVal = 0
    votee = ""
    if key in votes:
        votee = votes[key]
    if key in worth:
	worthVal = worth[key]
    if votee != "":
        persons[votee] += int(worthVal)

keylist = persons.keys()
keylist.sort()

for key in keylist:
    print key, "\t", persons[key]
