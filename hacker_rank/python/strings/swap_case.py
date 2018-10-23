# Problem: https://www.hackerrank.com/challenges/swap-case

msg = raw_input()
new = ""
for i in range(0, len(msg)):
    new += msg[i].swapcase()
print new