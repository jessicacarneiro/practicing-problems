chain = []
for x in xrange(1,10**6):
  first = x
  num = x
  total = 1
  while num != 1:
    if num % 2 == 0:
      num = num/2
    else:
      num = 3*num + 1
    total += 1
  chain.append((first,total))

larger = (0,0)
for x in xrange(0,len(chain)):
  if chain[x][1] > larger[1]:
    larger = chain[x]

print larger