n = 1
for i in range(2,101):
  n = n * i

# n to string
nstr = str(n)

sum = 0
for c in nstr:
  sum = sum + int(c)

print sum
