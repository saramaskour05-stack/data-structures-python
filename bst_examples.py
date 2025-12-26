"""
Binary Search Tree (BST) Examples in Python
Academic implementations from Data Structures coursework
"""

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

# Add a node to BST
def add_node(root, data):
    if root is None:
        return Node(data)
    if data < root.data:
        root.left = add_node(root.left, data)
    else:
        root.right = add_node(root.right, data)
    return root

# Search for a value in BST
def search_bst(root, target):
    if root is None:
        return False
    if root.data == target:
        return True
    elif target < root.data:
        return search_bst(root.left, target)
    else:
        return search_bst(root.right, target)

# Inorder Traversal
def inorder_traversal(root):
    if root:
        inorder_traversal(root.left)
        print(root.data, end=' ')
        inorder_traversal(root.right)

# Preorder Traversal
def preorder_traversal(root):
    if root:
        print(root.data, end=' ')
        preorder_traversal(root.left)
        preorder_traversal(root.right)

# Postorder Traversal
def postorder_traversal(root):
    if root:
        postorder_traversal(root.left)
        postorder_traversal(root.right)
        print(root.data, end=' ')

# Find minimum value
def find_min(root):
    if root.left is None:
        return root.data
    return find_min(root.left)

# Find maximum value
def find_max(root):
    if root.right is None:
        return root.data
    return find_max(root.right)

# Count nodes
def count_nodes(root):
    if root is None:
        return 0
    return 1 + count_nodes(root.left) + count_nodes(root.right)

# Check if BST is balanced
def find_height(root):
    if root is None:
        return -1
    left_height = find_height(root.left)
    right_height = find_height(root.right)
    return 1 + max(left_height, right_height)

def is_balanced(root):
    if root is None:
        return True
    left_height = find_height(root.left)
    right_height = find_height(root.right)
    if abs(left_height - right_height) > 1:
        return False
    return is_balanced(root.left) and is_balanced(root.right)
