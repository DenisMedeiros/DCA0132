#!/usr/bin/env python
import sys
# Read each line from stdin
for line in sys.stdin:
  # Get the words in each line
  words = line.split(",")
  name = words[1][:-1:] + " " + words[0][1::] 
  salary = words[6][1::]
  
  print '{0}\t{1}'.format(name, salary)
