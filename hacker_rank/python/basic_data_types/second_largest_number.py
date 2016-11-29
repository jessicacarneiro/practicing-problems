# Enter your code here. Read input from STDIN. Print output to STDOUT
n = int(raw_input())
nums = map(int,raw_input().strip().split(' '))
nums.sort()
nums.reverse()

largest = nums[0]
for i in range(1,len(nums)):
    if nums[i] != largest:
        print nums[i]
        break