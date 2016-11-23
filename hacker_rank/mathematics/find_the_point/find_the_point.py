n = int(raw_input())
r = []

for i in range(0,n):
    x1,y1,x2,y2 = map(int, raw_input().split())
    rx = 2*x2 - x1
    ry = 2*y2 - y1
    r.append(rx)
    r.append(ry)

for j in range(0,len(r),2):
    print str(r[j]) + " " + str(r[j+1])