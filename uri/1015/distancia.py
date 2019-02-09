from math import sqrt, pow

x1, y1 = raw_input().split()
x2, y2 = raw_input().split()
x1 = float(x1)
y1 = float(y1)
x2 = float(x2)
y2 = float(y2)

total = sqrt(pow(x2-x1,2) + pow(y2-y1,2))
print "{:.4f}".format(total)