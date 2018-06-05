#!/usr/bin/env python
import sys
# Read each line from stdin
for line in sys.stdin:
  # Get the words in each line
  words = line.split()
  filename = words[1][1::]
  
  print '{0}\t{1}'.format(filename, 1)
