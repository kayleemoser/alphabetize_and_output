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

def longest_word(column):
    word = 0
    for i in range(0,len(column)):
        if (len(column[i]) > word):
            word = len(column[i])
    return word

longest_a = longest_word(col_a)
longest_b = longest_word(col_b)
longest_c = longest_word(col_c)

# create string to print per row
for i in range(0,col_a_len):
    # column a will always be longest
    retStr = col_a[i].ljust(longest_a+1)
    if (i < col_b_len):
      retStr += col_b[i].ljust(longest_b+1)
    if (i < col_c_len):
      retStr += col_c[i].ljust(longest_c+1)

    print retStr







