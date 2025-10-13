#Binary Tree
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

# inorder traversal function (outside the class)
def inorder(root):
    if root:
        inorder(root.left)
        print(root.data, end="-")
        inorder(root.right)


# create the tree
root = Node(10)
root.left = Node(20)
root.right = Node(30)
root.left.left = Node(40)
root.left.right = Node(50)   # corrected duplicate 40 to 50

# call inorder traversal
inorder(root)


#binary search tree
class BSTNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

# Insert function (outside the class)
def insert(root, key):
    if root is None:
        return BSTNode(key)
    if key < root.data:
        root.left = insert(root.left, key)
    else:
        root.right = insert(root.right, key)
    return root

# Inorder traversal (outside the class)
def inorder(root):
    if root:
        inorder(root.left)
        print(root.data, end=" ")
        inorder(root.right)


# Driver code
root = None
for val in [50, 30, 70, 20, 40, 60, 80]:
    root = insert(root, val)

inorder(root)
