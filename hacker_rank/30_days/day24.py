class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
class Solution:
    def insert(self,head,data):
        p = Node(data)        
        if head==None:
            head=p
        elif head.next==None:
            head.next=p
        else:
            start=head
            while(start.next!=None):
                 start=start.next
            start.next=p
        return head 
    def display(self,head):
        current = head
        while current:
            print current.data,
            current = current.next  


    def removeDuplicates(self,head):
        if head == None:
            return head
        
        i = 0
        values = {}
        values.update({head.data:i})
        cur = head.next
        prev = head
        
        while cur != None:
            if values.has_key(cur.data):
                prev.next = cur.next
                cur = prev.next
            else:
                i += 1
                values.update({cur.data:i})
                prev = prev.next
                cur = prev.next
        return head
      
  
mylist= Solution()
T=int(input())
head=None
for i in range(T):
    data=int(input())
    head=mylist.insert(head,data)   
head=mylist.removeDuplicates(head)
mylist.display(head);