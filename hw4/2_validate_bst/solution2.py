import sys
sys.path.append('../1_traversal')
from solution1 import Node, BST


def is_valid_bst(root):
    def validate(node, min_val, max_val):
        if node is None:
            return True
        
        if not (min_val < node.value < max_val):
            return False
        
        return (validate(node.left, min_val, node.value) and
                validate(node.right, node.value, max_val))
    
    return validate(root, float('-inf'), float('inf'))


def is_valid_bst_inorder(root):
    """Красивый способ бонусом"""
    if root is None:
        return True
    
    bst = BST()
    bst.root = root
    inorder_values = bst.in_order()
    
    for i in range(1, len(inorder_values)):
        if inorder_values[i] <= inorder_values[i-1]:
            return False
    
    return True

