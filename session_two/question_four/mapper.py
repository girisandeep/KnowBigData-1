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

    #Get the first and last char of the key
    #Check which one is lower and then print the key such that the lower character comes first (same 
    #can be done by reversing the logic such that the higher charcter comes first)
    #For example for two mirroring keys: ACGT and TGCA. The logic can print keys as either ACGT and ACGT.
    #Or TGCA and TGCA. That is, based on first and last characters you either reverse the key or print it as it is.
    if key[0] > key[len(key)-1]:
        key = key[::-1]

    print "{0}\t{1}".format(key, value)
