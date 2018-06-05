#!/usr/bin/env python
import sys

# Process each key-value pair from the mapper
curr_word = None
curr_count = 0
for line in sys.stdin:

    # Get the key and value from the current line
    word, count = line.split('\t')
    
    simple = word.replace(".html", "")
    if len(simple) <= 5:
      count = int(count)   
      if word == curr_word:
        curr_count += count
      else:
        if curr_word:
          print '{0}\t{1}'.format(curr_word, curr_count)
        curr_word = word
        curr_count = count

if curr_word == word:
    print '{0}\t{1}'.format(curr_word, curr_count)

