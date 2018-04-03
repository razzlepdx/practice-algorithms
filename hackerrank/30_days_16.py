#!/bin/python

S = raw_input().strip()


def convert_to_int(string):
    """ Attempts to convert the given string value to int. """
    try:
        return int(string)
    except:
        return "Bad String"


print convert_to_int(S)
