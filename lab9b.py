#Lab 9 Problem 2
# Write a program to implement the preorder, inorder, postorder traversal of a tree.
class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

# Pre-order traversal
def preOrder(root):
    if root:
        print(root.data, end=' ')
        preOrder(root.left)
        preOrder(root.right)

# In-order traversal
def inOrder(root):
    if root:
        inOrder(root.left)
        print(root.data, end=' ')
        inOrder(root.right)

# Post-order traversal
def postOrder(root):
    if root:
        postOrder(root.left)
        postOrder(root.right)
        print(root.data, end=' ')

# Add user values to list
def build():
    root_data = int(input("Enter the root value: "))
    root = TreeNode(root_data)
    queue = [root]
    while queue:
        current = queue.pop(0)
        left_value = input(f"Enter the left branch of {current.data} or enter N: ")
        if left_value.lower() != 'n':
            l = TreeNode(int(left_value))
            current.left = l
            queue.append(l)
        right_value = input(f"Enter the right branch of {current.data} or enter N: ")
        if right_value.lower() != 'n':
            r = TreeNode(int(right_value))
            current.right = r
            queue.append(r)
    return root

root = build()
print("Preorder Traversal:")
preOrder(root)
print()
print("Inorder Traversal:")
inOrder(root)
print()
print("Postorder Traversal:")
postOrder(root)
print()
