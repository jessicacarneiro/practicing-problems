from math import sqrt

def is_prime(n):
	for i in range(2,int(sqrt(n))+1):
		if(n % i == 0):
			return False
	return True


i = 1
k = 0
while k < 10001:
	i = i + 1
	if(is_prime(i)):
		k = k + 1
	
print i
	