#!/usr/bin/python

# Coding project for ice.com
# Kaylee Moser
# October 12, 2015
# Python version 2.7.10

import sys

# Define a function that finds the length of the longest
# word in a column (list).
def longest_word(column):
    word_len = 0
    for i in range(0,len(column)):
        if (len(column[i]) > word_len):
            word_len = len(column[i])
    return word_len

def main():
    # Place given arguments into list and sort alphabetically.
    sentence = sys.stdin.readline().split()
    sentence.sort()
    
    # Find column lengths.
    col_a_len = col_b_len = col_c_len = len(sentence)/3
    remainder = len(sentence)%3
    if (remainder >= 1):
        col_a_len += 1
    if (remainder >= 2):
        col_b_len += 1
    
    # Split into separate lists per column.
    col_a = sentence[:col_a_len]
    col_b = sentence[col_a_len:col_a_len+col_b_len]
    col_c = sentence[col_a_len+col_b_len:]
    
    # Find the longest word for each column to use when
    # formatting below
    longest_a = longest_word(col_a)
    longest_b = longest_word(col_b)
    longest_c = longest_word(col_c)
    
    # Create string to print per row.
    for i in range(0,col_a_len):
        # Column A will always be longest.
        ret_str = col_a[i].ljust(longest_a+1)
        if (i < col_b_len):
          ret_str += col_b[i].ljust(longest_b+1)
        if (i < col_c_len):
          ret_str += col_c[i].ljust(longest_c+1)
    
        print ret_str

if (__name__ == '__main__'):
    main()






