#!/bin/python

import sys, re

names = []
N = int(raw_input().strip())
for a0 in xrange(N):
    pattern = re.compile(r'\b.*@gmail.com\b')
    firstName,emailID = raw_input().strip().split(' ')
    firstName,emailID = [str(firstName),str(emailID)]
    
    if pattern.match(emailID) != None:
        names.append(firstName)
        
names.sort()
for name in names:
    print name