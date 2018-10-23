for a in xrange(1000):
  for b in xrange(1000):
    for c in xrange(1000):
      if c > b and b > a:
        if (a + b + c == 1000):
          if (a**a + b**b == c**c):
            print a
            print b
            print c
            break