# Enter your code here. Read input from STDIN. Print output to STDOUT
n = int(raw_input())
elem = map(int,raw_input().strip().split(' '))
myTuple = tuple(elem)

print hash(myTuple)