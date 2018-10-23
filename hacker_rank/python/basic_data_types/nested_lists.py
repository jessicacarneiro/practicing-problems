n = int(raw_input())

s = []
for i in range(0,n):
  name = raw_input()
  grade = float(raw_input())
  s.append([name,grade])

s.sort(key=lambda x: x[1])

lowest = s[0][1]
second = 0
index = 0
for x in xrange(0,len(s)):
  if s[x][1] != lowest:
    second = s[x][1]
    index = x
    break

names = []
for x in xrange(index,len(s)):
  if s[x][1] == second:
    names.append(s[x][0])
  else:
    break

names.sort()
for x in xrange(0,len(names)):
  print names[x]