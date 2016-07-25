class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
class Solution:
    def display(self,head):
        current = head
        while current:
            print current.data,
            current = current.next

    def insert(self,head,data):
        
        if head == None:
            new_node = Node(data)
            head = new_node
            return head
        
        next_node = head
        while next_node.next != None:
            next_node = next_node.next
        new_node = Node(data)
        next_node.next = new_node
        return head

mylist= Solution()
T=int(input())
head=None
for i in range(T):
    data=int(input())
    head=mylist.insert(head,data)    
mylist.display(head);