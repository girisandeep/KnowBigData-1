#!/usr/bin/python

import sys

oldKey = None
usernames = []

# Loop around the data
# It will be in the format key\tval
# Where key is the DNA in sorted character order, val is the username
#
# Print all the words whose DNAs are equal

for line in sys.stdin:
    data_mapped = line.strip().split("\t")
    if len(data_mapped) != 2:
        # Something has gone wrong. Skip this line.
        continue

    thisKey, thisUser = data_mapped

    if oldKey and oldKey != thisKey:
	usernames.sort()
	print usernames, "\t", oldKey
        usernames = []

    oldKey = thisKey
    usernames.append(thisUser)

if oldKey != None:
    usernames.sort()
    print usernames, "\t", oldKey


