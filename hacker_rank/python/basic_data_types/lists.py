myList = []
n = int(raw_input())

for i in range(0,n):
    command = raw_input()
    command = command.split(" ")
    if command[0] == "pop":
        myList.pop()
    elif command[0] == "sort":
        myList.sort()
    elif command[0] == "print":
        print myList
    elif command[0] == "reverse":
        myList.reverse()
    elif command[0] == "insert":
        myList.insert(int(command[1]),int(command[2]))
    elif command[0] == "append":
        myList.append(int(command[1]))
    elif command[0] == "remove":
        myList.remove(int(command[1]))
    else:
        continue