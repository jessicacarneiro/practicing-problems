#!/bin/python

import sys

def swap(arr, i, j):
    temp = arr[i]
    arr[i] = arr[j]
    arr[j] = temp

n = int(raw_input().strip())
a = map(int,raw_input().strip().split(' '))

total_swaps = 0
for i in range(n):
    swaps = 0
    for j in range(n-1):
        if a[j] > a[j+1]:
            swap(a,j,j+1)
            swaps += 1
            total_swaps += 1
    if swaps == 0:
        break

print "Array is sorted in " + str(total_swaps) + " swaps."
print "First Element: " + str(a[0])
print "Last Element: " + str(a[-1])