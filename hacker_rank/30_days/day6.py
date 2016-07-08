import sys

n = input()

arr = [] 

for i in range(0,n):
    s = raw_input()
    arr.append(s)

for i in range(0,len(arr)):
    for k in range(0,len(arr[i])):
        if k % 2 == 0:
            sys.stdout.write(arr[i][k])
    sys.stdout.write(" ")
    for k in range(0,len(arr[i])):
        if k % 2 == 1:
            sys.stdout.write(arr[i][k])
    print