from math import sqrt

# Check if n is prime for n > 2
def isPrime(n):
  for i in range(2, int(sqrt(n))):
    if n % i == 0:
      return False
  return True

sum = 2
for i in range(3, 2000001): # [2,2*10^6]
  if isPrime(i):
    sum = sum + i

print sum