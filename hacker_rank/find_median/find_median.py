n = int(raw_input().strip())
arr = map(int,raw_input().strip().split(' '))

k = n/2
for i in range(0, k+1):
    minIndex = i
    minValue = arr[i]
    for j in range(i+1, n):
        if arr[j] < minValue:
            minIndex = j
            minValue = arr[j]
    temp = arr[minIndex]
    arr[minIndex] = arr[i]
    arr[i] = temp

print arr[n/2]
            