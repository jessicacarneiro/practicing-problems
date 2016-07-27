from math import sqrt
n = input()

for i in range(n):
    flag = True
    num = input()

    if num == 1:
        print "Not prime"
        continue
    
    for j in range(2,int(sqrt(num))+1):
        if num % j == 0:
            flag = False 
            break
    if flag:
        print "Prime"
    else:
        print "Not prime"