n = int(raw_input())

s = []
for i in range(0,n):
  student = raw_input()
  student = student.split(" ")
  s.append(student)

averages = {}
for i in range(0,len(s)):
  sum = 0
  size = float(len(s[i]) -1)
  for j in range(1,len(s[i])):
    sum += float(s[i][j])
  a = sum/size
  averages[s[i][0]] = a

name = raw_input()
if averages.has_key(name):
  print "%.2f" % averages[name]
