#!/bin/python


def factorial(n):
    """ Given an integer n, recursively finds the value of n! """
    if n == 1:
        return n

    return n * factorial(n-1)

if __name__ == "__main__":
    n = int(raw_input().strip())
    result = factorial(n)
    print result
