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

    print "{0}\t{1}".format(key, value)
