# Binary tree node class
class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

# Inorder Traversal (Non-Recursive) - Left, Root, Right
def inorder_iterative(root):
    stack = []
    current = root
    result = []

    while current or stack:
        # Traverse the left subtree
        while current:
            stack.append(current)
            current = current.left
        
        # Visit the root node
        current = stack.pop()
        result.append(current.val)
        
        # Traverse the right subtree
        current = current.right

    return result

# Preorder Traversal (Non-Recursive) - Root, Left, Right
def preorder_iterative(root):
    if not root:
        return []
    
    stack = [root]
    result = []

    while stack:
        # Visit the root node
        current = stack.pop()
        result.append(current.val)

        # Push right child first so left child is processed first
        if current.right:
            stack.append(current.right)
        if current.left:
            stack.append(current.left)

    return result

# Postorder Traversal (Non-Recursive, Two-Stack) - Left, Right, Root
def postorder_iterative(root):
    if not root:
        return []
    
    stack1 = [root]
    stack2 = []
    result = []

    while stack1:
        current = stack1.pop()
        stack2.append(current)

        # Push left and right children to the first stack
        if current.left:
            stack1.append(current.left)
        if current.right:
            stack1.append(current.right)

    # Stack2 will contain nodes in reverse postorder, so we pop them
    while stack2:
        result.append(stack2.pop().val)

    return result

# Function to create an example binary tree
def create_sample_tree():
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    root.right.left = Node(6)
    root.right.right = Node(7)
    return root

# Main code for testing
root = create_sample_tree()

print("Inorder Traversal (Iterative):", inorder_iterative(root))
print("Preorder Traversal (Iterative):", preorder_iterative(root))
print("Postorder Traversal (Iterative):", postorder_iterative(root))
