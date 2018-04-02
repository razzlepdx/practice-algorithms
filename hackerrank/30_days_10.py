#!/bin/python

n = int(raw_input().strip())


def convert_to_binary(num):
    """ Takes in a decimal number and returns it's corresponding binary number. """

    return bin(num)[2:]


def count_ones(num):
    """ Takes in test/user input as a decimal number and returns the number of
    consecutive ones that occur in its binary form."""

    binary_num = convert_to_binary(num)

    # this section seems unnecessary - will refactor for loop to remove conditionals
    #=====================
    if "1" in binary_num:
        max_consec = 1
    else:
        max_consec = 0

    current = max_consec
    #=====================

    for i in range(len(binary_num) - 1):
        if binary_num[i] == "1" and binary_num[i+1] == "1":
            current += 1
            if current == 1:
                current += 1
            if current > max_consec:
                max_consec = current
        else:
            current = 0

    return max_consec

# return response to STDOUT
print count_ones(n)
