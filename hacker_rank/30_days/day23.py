import sys

class Node:
    def __init__(self,data):
        self.right=self.left=None
        self.data = data
class Solution:
    def insert(self,root,data):
        if root==None:
            return Node(data)
        else:
            if data<=root.data:
                cur=self.insert(root.left,data)
                root.left=cur
            else:
                cur=self.insert(root.right,data)
                root.right=cur
        return root

    def levelOrder(self,root):
        if root==None:
            return
        nodes = []
        nodes.append(root)

        while len(nodes) > 0:
            r = nodes.pop(0)
            print r.data,

            if r.left != None:
                nodes.append(r.left)
            if r.right != None:
                nodes.append(r.right)


    def postOrder(self,root):
        if root==None:
            return
        else:
            print root.data,
            self.levelOrder(root.left)
            self.levelOrder(root.right)

T=int(raw_input())
myTree=Solution()
root=None
for i in range(T):
    data=int(raw_input())
    root=myTree.insert(root,data)
myTree.levelOrder(root)