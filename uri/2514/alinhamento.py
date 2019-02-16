def gcd(a, b):
    if a < 0:
        a = -a
    if b < 0:
        b = -b
    if b:
        while a and b:
            try:
                a = a%b
                b = b%a
            except ZeroDivisionError:
                break
    return (a + b)

def lcm(a, b, c):
    lcm = (a*b)/gcd(a, b)
    lcm = (int(lcm)*c)/gcd(int(lcm), c)
    return int(lcm)

results = []
while True:
    try:
        m = int(input())
        l = raw_input()
        l1, l2, l3 = l.split()
        results.append(abs(m - lcm(int(l1), int(l2), int(l3))))
    except EOFError:
        break

for r in results:
    print r