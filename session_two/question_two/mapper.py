#!/usr/bin/python

# Format of each line is:
# split the line by whitespaces
#
# We want elements key (all characters of the word in a sorted order) and value (the actual word)
# We need to write them out to standard output, separated by a tab

import sys

for line in sys.stdin:
    data = line.strip().split(" ")
    for word in data:
	char_array = []
	i = 0
	while (i != len(word)):
		char_array.append(word[i])
		i += 1
	char_array.sort()
	key = ""

	i = 0
        while (i != len(char_array)):
                key += char_array[i]
                i += 1    

        print "{0}\t{1}".format(key, word)
