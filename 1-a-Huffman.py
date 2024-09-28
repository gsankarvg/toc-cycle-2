import heapq
from collections import defaultdict, Counter

class Node:
    def __init__(self, char, freq):
        self.char = char
        self.freq = freq
        self.left = None
        self.right = None
    
    # Defining comparator to make Node instances comparable based on frequency
    def __lt__(self, other):
        return self.freq < other.freq

# Function to build Huffman Tree
def build_huffman_tree(frequencies):
    heap = [Node(char, freq) for char, freq in frequencies.items()]
    heapq.heapify(heap)
    
    while len(heap) > 1:
        node1 = heapq.heappop(heap)
        node2 = heapq.heappop(heap)
        
        merged = Node(None, node1.freq + node2.freq)
        merged.left = node1
        merged.right = node2
        heapq.heappush(heap, merged)
    
    return heap[0]

# Function to generate Huffman codes from the tree
def generate_huffman_codes(node, prefix="", code_map=None):
    if code_map is None:
        code_map = {}
    if node is not None:
        if node.char is not None:
            code_map[node.char] = prefix
        generate_huffman_codes(node.left, prefix + "0", code_map)
        generate_huffman_codes(node.right, prefix + "1", code_map)
    return code_map

# Generalized function for Huffman coding
def huffman_coding(data):
    frequencies = Counter(data)
    huffman_tree = build_huffman_tree(frequencies)
    huffman_codes = generate_huffman_codes(huffman_tree)
    return huffman_codes

# Example usage
data = "greedyalgorithm"
codes = huffman_coding(data)
print("Huffman Codes:", codes)
