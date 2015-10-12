#!/usr/bin/python

# Coding project for ice.com
# Kaylee Moser
# October 9, 2015
# Python version 2.7.10

import sys

# place given arguments into list
sentence = sys.argv[1:]

# sort alphabetically
sentence.sort()

# find column lengths
col_a_len = col_b_len = col_c_len = len(sentence)/3
remainder = len(sentence)%3
if (remainder >= 1):
    col_a_len += 1
if (remainder >= 2):
    col_b_len += 1

# split into lists per column
col_a = sentence[:col_a_len]
col_b = sentence[col_a_len:col_a_len+col_b_len]
col_c = sentence[col_a_len+col_b_len:]

# create string to print per row
for i in range(0,col_a_len):
    # column a will always be longest
    retStr = col_a[i].ljust(10)
    
    if (i < col_b_len):
      retStr += col_b[i].ljust(10)
    if (i < col_c_len):
      retStr += col_c[i].ljust(10)

    print retStr







