from math import sqrt

n = 600851475143
factors = []

'''Returns false if n is divisible by 
a number that is not itself or 1'''
def is_prime(n):
	for i in range(2,int(sqrt(n))+1):
		if(n % i == 0):
			return False
	return True

for i in range(2,int(sqrt(n))):
	if(n % i == 0):
		if(is_prime(i)):
			factors.append(i)

factors.sort()

print factors[-1]	