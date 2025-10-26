import pytest
import sys
sys.path.append('../1_traversal')
from solution1 import Node
from solution2 import is_valid_bst, is_valid_bst_inorder


def test_empty_tree():
    assert is_valid_bst(None) == True
    assert is_valid_bst_inorder(None) == True


def test_single_node():
    root = Node(10)
    assert is_valid_bst(root) == True
    assert is_valid_bst_inorder(root) == True


def test_simple_valid_bst():
    root = Node(2)
    root.left = Node(1)
    root.right = Node(3)
    assert is_valid_bst(root) == True
    assert is_valid_bst_inorder(root) == True


def test_simple_invalid_bst_local_violation():
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    assert is_valid_bst(root) == False
    assert is_valid_bst_inorder(root) == False


def test_global_violation():
    root = Node(10)
    root.left = Node(5)
    root.right = Node(20)
    root.right.left = Node(8)
    root.right.right = Node(25)
    
    assert is_valid_bst(root) == False
    assert is_valid_bst_inorder(root) == False


def test_global_violation_left_subtree():
    root = Node(10)
    root.left = Node(5)
    root.left.left = Node(3)
    root.left.right = Node(15)
    root.right = Node(20)
    
    assert is_valid_bst(root) == False
    assert is_valid_bst_inorder(root) == False


def test_left_skewed_valid():
    root = Node(10)
    root.left = Node(8)
    root.left.left = Node(6)
    root.left.left.left = Node(4)
    
    assert is_valid_bst(root) == True
    assert is_valid_bst_inorder(root) == True


def test_right_skewed_valid():
    root = Node(4)
    root.right = Node(6)
    root.right.right = Node(8)
    root.right.right.right = Node(10)
    
    assert is_valid_bst(root) == True
    assert is_valid_bst_inorder(root) == True


def test_left_skewed_invalid():
    root = Node(10)
    root.left = Node(8)
    root.left.left = Node(6)
    root.left.left.right = Node(7)
    root.left.left.right.right = Node(9)
    
    assert is_valid_bst(root) == False
    assert is_valid_bst_inorder(root) == False


def test_duplicate_in_root():
    root = Node(10)
    root.left = Node(5)
    root.right = Node(10)
    assert is_valid_bst(root) == False
    assert is_valid_bst_inorder(root) == False


def test_duplicate_in_left():
    root = Node(10)
    root.left = Node(5)
    root.right = Node(15)
    root.left.left = Node(5)
    assert is_valid_bst(root) == False
    assert is_valid_bst_inorder(root) == False


def test_duplicate_in_right():
    root = Node(10)
    root.left = Node(5)
    root.right = Node(15)
    root.right.right = Node(15)
    assert is_valid_bst(root) == False
    assert is_valid_bst_inorder(root) == False


def test_all_duplicates():
    root = Node(2)
    root.left = Node(2)
    root.right = Node(2)
    assert is_valid_bst(root) == False
    assert is_valid_bst_inorder(root) == False


def test_complex_valid_bst():
    root = Node(50)
    root.left = Node(30)
    root.right = Node(70)
    root.left.left = Node(20)
    root.left.right = Node(40)
    root.right.left = Node(60)
    root.right.right = Node(80)
    root.left.left.left = Node(10)
    root.left.left.right = Node(25)
    
    assert is_valid_bst(root) == True
    assert is_valid_bst_inorder(root) == True


def test_complex_invalid_bst_deep_violation():
    root = Node(50)
    root.left = Node(30)
    root.right = Node(70)
    root.left.left = Node(20)
    root.left.right = Node(40)
    root.right.left = Node(60)
    root.right.right = Node(80)
    root.left.left.left = Node(10)
    root.left.left.right = Node(55)
    
    assert is_valid_bst(root) == False
    assert is_valid_bst_inorder(root) == False


def test_negative_values():
    root = Node(0)
    root.left = Node(-10)
    root.right = Node(10)
    root.left.left = Node(-20)
    root.left.right = Node(-5)
    
    assert is_valid_bst(root) == True
    assert is_valid_bst_inorder(root) == True


def test_negative_values_invalid():
    root = Node(0)
    root.left = Node(-10)
    root.right = Node(10)
    root.left.left = Node(-20)
    root.left.right = Node(5)
    
    assert is_valid_bst(root) == False
    assert is_valid_bst_inorder(root) == False


def test_large_values():
    root = Node(10**9)
    root.left = Node(10**8)
    root.right = Node(10**10)
    assert is_valid_bst(root) == True
    assert is_valid_bst_inorder(root) == True


def test_boundary_values_valid():
    root = Node(0)
    root.left = Node(-2**31)
    root.right = Node(2**31 - 1)
    
    assert is_valid_bst(root) == True
    assert is_valid_bst_inorder(root) == True


def test_only_left_children():
    root = Node(10)
    root.left = Node(5)
    root.left.left = Node(3)
    root.left.left.left = Node(1)
    
    assert is_valid_bst(root) == True
    assert is_valid_bst_inorder(root) == True


def test_only_right_children():
    root = Node(1)
    root.right = Node(3)
    root.right.right = Node(5)
    root.right.right.right = Node(10)
    
    assert is_valid_bst(root) == True
    assert is_valid_bst_inorder(root) == True


def test_zigzag_valid():
    root = Node(10)
    root.left = Node(5)
    root.left.right = Node(7)
    root.left.right.left = Node(6)
    
    assert is_valid_bst(root) == True
    assert is_valid_bst_inorder(root) == True


def test_zigzag_invalid():
    root = Node(10)
    root.left = Node(5)
    root.left.right = Node(7)
    root.left.right.left = Node(12)
    
    assert is_valid_bst(root) == False
    assert is_valid_bst_inorder(root) == False


def test_equal_at_boundary():
    root = Node(5)
    root.left = Node(4)
    root.right = Node(6)
    root.left.left = Node(4)
    
    assert is_valid_bst(root) == False
    assert is_valid_bst_inorder(root) == False


def test_float_values():
    root = Node(5.5)
    root.left = Node(2.3)
    root.right = Node(7.8)
    root.left.left = Node(1.1)
    root.right.right = Node(9.9)
    
    assert is_valid_bst(root) == True
    assert is_valid_bst_inorder(root) == True


def test_float_values_invalid():
    root = Node(5.5)
    root.left = Node(2.3)
    root.right = Node(7.8)
    root.left.right = Node(5.5)
    
    assert is_valid_bst(root) == False
    assert is_valid_bst_inorder(root) == False


def test_minimal_invalid():
    root = Node(1)
    root.right = Node(1)
    assert is_valid_bst(root) == False
    assert is_valid_bst_inorder(root) == False


def test_two_nodes_valid_left():
    root = Node(10)
    root.left = Node(5)
    assert is_valid_bst(root) == True
    assert is_valid_bst_inorder(root) == True


def test_two_nodes_valid_right():
    root = Node(5)
    root.right = Node(10)
    assert is_valid_bst(root) == True
    assert is_valid_bst_inorder(root) == True


def test_two_nodes_invalid_left():
    root = Node(5)
    root.left = Node(10)
    assert is_valid_bst(root) == False
    assert is_valid_bst_inorder(root) == False


def test_two_nodes_invalid_right():
    root = Node(10)
    root.right = Node(5)
    assert is_valid_bst(root) == False
    assert is_valid_bst_inorder(root) == False

