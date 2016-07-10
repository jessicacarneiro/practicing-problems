n = input()

dic = {}

for i in range(n):
    arr = map(str,raw_input().strip().split(' '))
    dic.update({arr[0]:arr[1]})

for i in range(n):
    name = raw_input()
    if(dic.has_key(name)):
        print name + "=" + dic[name]
    else:
        print "Not found"