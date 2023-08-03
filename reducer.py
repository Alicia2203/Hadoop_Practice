#!/usr/bin/env python3

from operator import itemgetter
import sys

# Initialize variables to keep track of the current word and its count
current_word = None
current_count = 0
word = None

for line in sys.stdin:
    # Remove leading and trailing whitespaces from the line
    line = line.strip()

    # Split the line into word and count based on the tab character
    word, count = line.split('\t', 1)

    try:
        count = int(count)
    except ValueError:
        continue

    if current_word == word:
        current_count += count
    else:
        if current_word:
            # If the current word is different from the previous word and it is not None,
            # print the previous word and its total count
            print('%s\t%s' % (current_word, current_count))

        # Reset the current word and count to the new word and its count
        current_count = count
        current_word = word

# After reading all lines, print the last word and its total count
if current_word == word:
	print('%s\t%s' % (current_word, current_count))
