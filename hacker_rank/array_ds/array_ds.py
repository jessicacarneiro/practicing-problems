#!/bin/python

import sys


n = int(raw_input().strip())
arr = map(int,raw_input().strip().split(' '))

for i in reversed(range(0,len(arr))):
    print arr[i],