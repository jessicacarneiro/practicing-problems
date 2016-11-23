sum = 0
n1 = 1
n2 = 1
while n2 < 4*10**6:
  if n2 % 2 == 0:
    sum = sum + n2
  temp = n2
  n2 = n1 + n2
  n1 = temp

print sum