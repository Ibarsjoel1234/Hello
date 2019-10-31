class Node:
    def __init__(self,key):
        self.left  = None
        self.right = None
        self.val = key
        
def insert(root,node):
    if root is None:
        root = node
    else:
        if root.val < node.val:
            if root.right is None:
                root.right = node
            else:
                insert(root.right,node)
        else:
            if root.left is None:
                root.left = node
            else:
                insert(root.left,node)
def inorder(root): 
    if root: 
        inorder(root.left) 
        print(root.val) 
        inorder(root.right) 
        
r = eval(input("Enter the node:"))
r = Node(r)
a = eval(input("Values: "))
b = eval(input("values2: "))
c = eval(input("values3: "))
d = eval(input("value4: "))
e = eval(input("value5: "))
f = eval(input("value6: "))
insert(r,Node(a))
insert(r,Node(b))
insert(r,Node(c))
insert(r,Node(d))
insert(r,Node(e))
insert(r,Node(f))
inorder(r)
