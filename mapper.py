#!/usr/bin/env python3
import sys
import re

# Read each line from the input stream (stdin)
for line in sys.stdin:
    # Remove leading and trailing whitespaces
    line = line.strip()

    # Remove non-word characters from the line
    cleaned_line = re.sub(r'[^\w\s]', '', line)

    # Split the cleaned line into individual words based on spaces
    words = cleaned_line.split()

    # Emit each word with an initial count of 1, separated by a tab character
    for word in words:
        print('%s\t%s' % (word, 1))
