#!/usr/bin/python

# Format of each line is:
# split the line by whitespaces
#
# We want elements key (DNA sequences) and value (user)
# We need to write them out to standard output, separated by a tab

import sys

for line in sys.stdin:
    data = line.strip().split(" ")
    if len(data) != 2:
        continue

    value, key = data
    reverseKey = key[::-1]
    
    #Get the actual key and create a reverse of that key. Now, find the minimum of those two keys.
    #For example, if Key=ACGT then reverse will be TGCA. The minumum of those will be ACGT.
    #In doing this, we will get all the keys and even the mirrored ones for form a unique key value pair.
    #Reducer will then use this output to compure user with same or mirrored DNAs
    key = min(key, reverseKey)

    print "{0}\t{1}".format(key, value)

