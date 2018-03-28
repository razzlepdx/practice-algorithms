#!/bin/python
# Task
# Given an array, A, of N integers, print A's elements in
# reverse order as a single line of space-separated numbers.

n = int(raw_input().strip())
arr = map(int, raw_input().strip().split(' '))

result = ""

for item in arr:
    result = str(item) + " " + result

print result
