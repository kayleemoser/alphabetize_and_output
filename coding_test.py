#!/usr/bin/python

# Coding project for ice.com
# Kaylee Moser
# October 9, 2015
# Python version 2.7.10

import sys

# place given arguments into list
sentence = sys.argv
sentence.pop(0)

# sort alphabetically
sentence.sort()

# initialize columns for output
col_a = []
col_b = []
col_c = []

sentence_len = len(sentence)
col_a_len = col_b_len = col_c_len = sentence_len/3
col_rem = sentence_len%3

if (col_rem >= 1):
    col_a_len += 1
if (col_rem >= 2):
    col_b_len += 1



print sentence
