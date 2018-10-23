#!/bin/python

import sys

n = int(raw_input().strip())

def convert_to_binary(n):
    q = n
    bin = ""
    while q > 1:
        bin = bin + str(q % 2)
        q = q/2
    bin = bin + str(q)
    bin = bin[::-1]
    return bin

bin = convert_to_binary(n)

prev_max = 0
i = 0
while True:
    max = 0
    if i >= len(bin):
        break
    while i < len(bin) and bin[i] == '1':
        max += 1
        i += 1
    if max > prev_max:
        prev_max = max
    i += 1

print prev_max       
