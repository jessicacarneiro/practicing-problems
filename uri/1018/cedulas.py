bills = [100, 50, 20, 10, 5, 2, 1]
amount = [0,   0,  0,  0, 0, 0, 0]
value = int(input())

i = 0
total = 0
left = value
while left > 0 and i < len(bills):
    if bills[i] <= left:
        left -= bills[i]
        amount[i] += 1
    else:
        i += 1

print value
for i in range(0, len(amount)):
    print "{} nota(s) de R$ {},00".format(amount[i], bills[i])