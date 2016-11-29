# Enter your code here. Read input from STDIN. Print output to STDOUT
i = int(raw_input())

hey = ""
for i in range(1,i+1):
    hey += str(i)
print hey

# alternative in Python 3 in one line:
# print(*range(1, int(input())+1), sep='')