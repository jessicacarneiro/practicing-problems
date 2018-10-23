#!/bin/python

import sys

S = raw_input().strip()

try:
    number = int(S)
    print str(number)
except Exception:
    print "Bad String"