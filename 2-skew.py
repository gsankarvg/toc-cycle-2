class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

# Function to create a left-skewed binary tree
def create_left_skewed_tree(height):
    root = Node(1)
    current = root
    for i in range(2, height + 2):
        current.left = Node(i)
        current = current.left
    return root

# Function to display the tree in inorder traversal
def inorder_traversal(root):
    if root is None:
        return []
    return inorder_traversal(root.left) + [root.val] + inorder_traversal(root.right)

# Function to create a balanced binary tree from a sorted array
def sorted_array_to_bst(arr):
    if not arr:
        return None
    
    mid = len(arr) // 2
    root = Node(arr[mid])
    
    root.left = sorted_array_to_bst(arr[:mid])
    root.right = sorted_array_to_bst(arr[mid + 1:])
    
    return root

# Convert left-skewed tree to height-balanced tree
def convert_to_balanced_tree(root):
    inorder_vals = inorder_traversal(root)  # Get sorted values from the skewed tree
    return sorted_array_to_bst(inorder_vals)

# Function to search for a key in a binary tree and count the number of comparisons
def search_tree(root, key):
    comparisons = 0
    current = root
    while current:
        comparisons += 1
        if current.val == key:
            return comparisons
        elif key < current.val:
            current = current.left
        else:
            current = current.right
    return comparisons  # If not found, return the comparisons made

# Main Code

# Step 1: Create a left-skewed binary tree with minimum height 4
left_skewed_tree = create_left_skewed_tree(4)

# Step 2: Convert the left-skewed binary tree into a height-balanced tree
balanced_tree = convert_to_balanced_tree(left_skewed_tree)

# Step 3: Search for two elements (example: 3 and 5) in both trees and compare the number of comparisons
key1, key2 = 3, 5

# Searching in left-skewed tree
comparisons_skewed_1 = search_tree(left_skewed_tree, key1)
comparisons_skewed_2 = search_tree(left_skewed_tree, key2)

# Searching in height-balanced tree
comparisons_balanced_1 = search_tree(balanced_tree, key1)
comparisons_balanced_2 = search_tree(balanced_tree, key2)

# Display the trees' inorder traversal (for verification) and comparison results
print("Inorder of Left-Skewed Tree:", inorder_traversal(left_skewed_tree))
print("Inorder of Height-Balanced Tree:", inorder_traversal(balanced_tree))

print(f"\nComparisons for {key1} in Left-Skewed Tree: {comparisons_skewed_1}")
print(f"Comparisons for {key2} in Left-Skewed Tree: {comparisons_skewed_2}")

print(f"\nComparisons for {key1} in Balanced Tree: {comparisons_balanced_1}")
print(f"Comparisons for {key2} in Balanced Tree: {comparisons_balanced_2}")
