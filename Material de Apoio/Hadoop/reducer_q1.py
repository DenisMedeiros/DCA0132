#!/usr/bin/env python
import sys

data = []

# Process each key-value pair from the mapper
for line in sys.stdin:

  try:
    # Get the key and value from the current line
    name, salary = line.split('\t')
    data.append([name, float(salary.strip())])

  except:
    pass

data.sort(key = lambda x: x[1], reverse=True)

for i in range(10):
  print '{0}\t{1}'.format(data[i][0], data[i][1])