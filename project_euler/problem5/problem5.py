'''
2520 is the smallest number that can be divided by each of the 
numbers from 1 to 10 without any remainder. What is the smallest 
positive number that is evenly divisible by all of the numbers from 1 to 20?
'''

def is_divible_20(n):
	for i in range(2,21):
		if(n % i != 0):
			return False
	return True

i = 2*3*2*5*7*2*3*11*13*2*17*19

while not is_divible_20(i):
	i = i + 1

print i