# Problem Description found at:
# https://www.hackerrank.com/challenges/30-sorting/problem
#!/bin/python


n = int(raw_input().strip())
a = map(int, raw_input().strip().split(' '))
# Write Your Code Here

total_swaps = 0

for i in range(n):
    current_swaps = 0
    for j in range(n - 1):
        first = a[j]
        second = a[j+1]
        if first > second:
            a[j], a[j+1] = second, first
            total_swaps += 1
            current_swaps += 1
    if current_swaps == 0:
        break;

print "Array is sorted in {} swaps.".format(total_swaps)
print "First Element: " + str(a[0])
print "Last Element: " + str(a[-1])
