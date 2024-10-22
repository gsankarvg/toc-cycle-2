class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

# Function to perform inorder traversal
def inorderTraversal(root):

    # Base case: if null
    if root is None:
        return

    # Recur on the left subtree
    inorderTraversal(root.left)

    # Visit the current node
    print(root.data, end=" ")

    # Recur on the right subtree
    inorderTraversal(root.right)

# Function to perform preorder traversal
def preorderTraversal(root):

    # Base case
    if root is None:
        return

    # Visit the current node
    print(root.data, end=' ')

    # Recur on the left subtree
    preorderTraversal(root.left)

    # Recur on the right subtree
    preorderTraversal(root.right)

def postorderTraversal(node):
    # Base case: if the current node is null, return
    if node is None:
        return
    # Recur on the left subtree
    postorderTraversal(node.left)
    # Recur on the right subtree
    postorderTraversal(node.right)
    # Visit the current node
    print(node.data, end=' ')

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
print("  inorder traversal : ",end='')
inorderTraversal(root)
print("\n preorder traversal: ",end='')
preorderTraversal(root)
print("\n postorder traversal ",end='')
postorderTraversal(root)
