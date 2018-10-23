#!/bin/python

import sys


n = int(raw_input().strip())
arr = map(int,raw_input().strip().split(' '))

sum = 0
for element in arr:
    sum = sum + element
    
print sum