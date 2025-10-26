import sys
sys.path.append('../1_traversal')
from solution1 import Node


def is_balanced(root):
    def get_height_if_balanced(node):
        if node is None:
            return 0
        
        left_height = get_height_if_balanced(node.left)
        if left_height == -1:
            return -1
        
        right_height = get_height_if_balanced(node.right)
        if right_height == -1:
            return -1
        
        if abs(left_height - right_height) > 1:
            return -1
        
        return 1 + max(left_height, right_height)
    
    return get_height_if_balanced(root) != -1

