value = input()
size = input()
arr = map(int,raw_input().strip().split(' '))

index = -1
for i in range(0, size):
    if arr[i] == value:
        index = i
        break
        
print index