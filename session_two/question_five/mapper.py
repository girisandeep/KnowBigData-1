#!/usr/bin/python

# Format of each line is:
# split the line by tab
# If it is list 1 then -> We want elements key (Voter), * (indicating that it is list1) and value (Votee)
# If it is list 2 then -> We want elements key (Person), # (indicating that it is list2) and value (Worth)
# We then output the data in tabbed format to the standard output

import sys

for line in sys.stdin:
    data = line.strip().split("\t")
    if len(data) != 2:
	continue

    key, value = data

    print "{0}\t{1}".format(key, value)
