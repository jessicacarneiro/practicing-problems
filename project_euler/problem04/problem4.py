def is_palindrome(n):
	j = len(n) - 1

	if(len(n) % 2 == 0):
		upper = len(n)/2 - 1
	else:
		upper = len(n)/2

	for i in range(0,upper+1):
		if(n[j] != n[i]):
			return False
		j = j - 1

	return True

i = 999
max = 0
while(i >= 100):
	j = 999
	while(j >= 100):
		product = i * j
		if(is_palindrome(str(product)) and product > max):
			max = product
		j = j - 1
	i = i - 1

print max