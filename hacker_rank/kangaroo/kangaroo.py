#!/bin/python

import sys


x1,v1,x2,v2 = raw_input().strip().split(' ')
x1,v1,x2,v2 = [int(x1),int(v1),int(x2),int(v2)]

catch = False
i = 10000
while x1 < 10000:
    x1 = x1 + v1
    x2 = x2 + v2
    if x1 == x2:
        catch = True
        break

if not catch:
    print "NO"
else:
    print "YES"