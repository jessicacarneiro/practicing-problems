#!/bin/python

import sys


n = int(raw_input().strip())
arr = map(int,raw_input().strip().split(' '))

for i in reversed(range(len(arr))):
    print arr[i],