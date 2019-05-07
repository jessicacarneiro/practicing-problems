from math import pow

for a in range(0, 500):
  for b in range(a + 1, 500):
    for c in range(b + 1, 500):
      if (a + b + c) == 1000:
        if (pow(c,2) == (pow(a,2) + pow(b,2))):
          print('a = {}, b = {}, c = {}'.format(a, b, c))
          print('a*b*c = {}'.format(a*b*c))
