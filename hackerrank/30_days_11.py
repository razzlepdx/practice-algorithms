#!/bin/python


arr = []

for arr_i in xrange(6):
    arr_temp = map(int, raw_input().strip().split(' '))
    arr.append(arr_temp)

a = arr
hour_glass = []
current_max = None

for i in range(len(a)-2):

    for j in range(len(a[i])-2):
        top_row = a[i][j:j+3]
        hour_glass.extend(top_row)

        mid_row = a[i+1][j+1]
        hour_glass.append(mid_row)

        bottom_row = a[i+2][j:j+3]
        hour_glass.extend(bottom_row)

        if current_max is None or sum(hour_glass) > current_max:
            current_max = sum(hour_glass)

        hour_glass = []

print current_max
