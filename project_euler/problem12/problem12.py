from math import sqrt

# returns the number of divisors
def countDivisors(n):
  count = 2
  for i in range(2,n/2+1):
    if n % i == 0:
      count = count + 1
  return count

# gets the smaller possible number
smaller = 1
for x in xrange(2,501):
  smaller = smaller * x

last = 8
triang = 28
found = False
while not found:
  if triang >= smaller:
    count = countDivisors(triang)
    if count >= 500:
      found = True
  triang = triang + last
  last = last + 1

print triang