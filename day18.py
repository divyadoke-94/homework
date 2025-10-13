class AVLNode:
    def __init__(self, key):
        self.data = key
        self.left = None
        self.right = None
        self.height = 1

    @staticmethod
    def get_height(node):
        if not node:
            return 0
        return node.height

    @staticmethod
    def get_balance(node):
        if not node:
            return 0
        return AVLNode.get_height(node.left) - AVLNode.get_height(node.right)

    @staticmethod
    def right_rotate(z):
        y = z.left
        T3 = y.right

        # Perform rotation
        y.right = z
        z.left = T3

        # Update heights
        z.height = 1 + max(AVLNode.get_height(z.left), AVLNode.get_height(z.right))
        y.height = 1 + max(AVLNode.get_height(y.left), AVLNode.get_height(y.right))

        return y

    @staticmethod
    def left_rotate(z):
        y = z.right
        T2 = y.left

        # Perform rotation
        y.left = z
        z.right = T2

        # Update heights
        z.height = 1 + max(AVLNode.get_height(z.left), AVLNode.get_height(z.right))
        y.height = 1 + max(AVLNode.get_height(y.left), AVLNode.get_height(y.right))

        return y

    @staticmethod
    def insert(root, key):
        # 1. Normal BST insertion
        if not root:
            return AVLNode(key)
        elif key < root.data:
            root.left = AVLNode.insert(root.left, key)
        else:
            root.right = AVLNode.insert(root.right, key)

        # 2. Update height
        root.height = 1 + max(AVLNode.get_height(root.left), AVLNode.get_height(root.right))

        # 3. Get balance factor
        balance = AVLNode.get_balance(root)

        # 4. Balance the tree
        # Left Left Case
        if balance > 1 and key < root.left.data:
            return AVLNode.right_rotate(root)

        # Right Right Case
        if balance < -1 and key > root.right.data:
            return AVLNode.left_rotate(root)

        # Left Right Case
        if balance > 1 and key > root.left.data:
            root.left = AVLNode.left_rotate(root.left)
            return AVLNode.right_rotate(root)

        # Right Left Case
        if balance < -1 and key < root.right.data:
            root.right = AVLNode.right_rotate(root.right)
            return AVLNode.left_rotate(root)

        return root


def inorder(root):
    if root:
        inorder(root.left)
        print(root.data, end=" ")
        inorder(root.right)


# Driver code
root = None
for val in [30, 20, 40, 10, 25, 50]:
    root = AVLNode.insert(root, val)

print("Inorder Traversal of AVL Tree:")
inorder(root)
