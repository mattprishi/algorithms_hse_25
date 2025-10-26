import pytest
import sys
sys.path.append('../1_traversal')
from solution1 import Node
from solution3 import is_balanced


def test_empty_tree():
    assert is_balanced(None) == True


def test_single_node():
    root = Node(1)
    assert is_balanced(root) == True


def test_two_nodes_left():
    root = Node(1)
    root.left = Node(2)
    assert is_balanced(root) == True


def test_two_nodes_right():
    root = Node(1)
    root.right = Node(2)
    assert is_balanced(root) == True


def test_perfect_tree_height_2():
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    assert is_balanced(root) == True


def test_perfect_tree_height_3():
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    root.right.left = Node(6)
    root.right.right = Node(7)
    assert is_balanced(root) == True


def test_balanced_diff_1():
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    assert is_balanced(root) == True


def test_balanced_diff_1_right():
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.right.right = Node(4)
    assert is_balanced(root) == True


def test_unbalanced_simple_left():
    root = Node(1)
    root.left = Node(2)
    root.left.left = Node(3)
    assert is_balanced(root) == False


def test_unbalanced_simple_right():
    root = Node(1)
    root.right = Node(2)
    root.right.right = Node(3)
    assert is_balanced(root) == False


def test_unbalanced_chain_left():
    root = Node(1)
    root.left = Node(2)
    root.left.left = Node(3)
    root.left.left.left = Node(4)
    assert is_balanced(root) == False


def test_unbalanced_chain_right():
    root = Node(1)
    root.right = Node(2)
    root.right.right = Node(3)
    root.right.right.right = Node(4)
    assert is_balanced(root) == False


def test_unbalanced_long_chain():
    root = Node(1)
    current = root
    for i in range(2, 11):
        current.left = Node(i)
        current = current.left
    assert is_balanced(root) == False


def test_balanced_zigzag():
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.right = Node(4)
    root.right.left = Node(5)
    assert is_balanced(root) == True


def test_balanced_comb():
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    root.right.right = Node(6)
    root.left.left.left = Node(7)
    root.left.left.right = Node(8)
    root.left.right.left = Node(9)
    assert is_balanced(root) == True


def test_unbalanced_deep_violation():
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    root.left.left.left = Node(6)
    root.left.left.left.left = Node(7)
    assert is_balanced(root) == False


def test_unbalanced_deep_right():
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.right.right = Node(4)
    root.right.right.right = Node(5)
    root.right.right.right.right = Node(6)
    assert is_balanced(root) == False


def test_balanced_height_diff_1_complex():
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    root.right.right = Node(6)
    root.left.left.left = Node(7)
    root.left.left.right = Node(8)
    assert is_balanced(root) == True


def test_unbalanced_grandchild():
    root = Node(1)
    root.left = Node(2)
    root.left.left = Node(3)
    root.left.left.left = Node(4)
    assert is_balanced(root) == False


def test_balanced_diff_0():
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    root.right.left = Node(6)
    root.right.right = Node(7)
    root.left.left.left = Node(8)
    root.left.left.right = Node(9)
    root.left.right.left = Node(10)
    root.left.right.right = Node(11)
    root.right.left.left = Node(12)
    root.right.left.right = Node(13)
    root.right.right.left = Node(14)
    root.right.right.right = Node(15)
    assert is_balanced(root) == True


def test_unbalanced_at_root():
    root = Node(1)
    root.left = Node(2)
    root.left.left = Node(3)
    root.left.right = Node(4)
    root.left.left.left = Node(5)
    assert is_balanced(root) == False


def test_balanced_one_sided_depth_1():
    root = Node(1)
    root.left = Node(2)
    root.left.left = Node(3)
    root.right = Node(4)
    assert is_balanced(root) == True


def test_unbalanced_one_sided_depth_2():
    root = Node(1)
    root.left = Node(2)
    root.left.left = Node(3)
    root.left.left.left = Node(4)
    root.right = Node(5)
    assert is_balanced(root) == False


def test_balanced_asymmetric():
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.right.left = Node(5)
    root.right.right = Node(6)
    assert is_balanced(root) == True


def test_unbalanced_subtle():
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.left.left = Node(5)
    root.right.right = Node(6)
    assert is_balanced(root) == False


def test_balanced_mirror():
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.left.left = Node(5)
    root.right.right = Node(6)
    root.right.right.right = Node(7)
    assert is_balanced(root) == False


def test_unbalanced_mirror_broken():
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.left.left = Node(5)
    root.left.left.left.left = Node(6)
    root.right.right = Node(7)
    root.right.right.right = Node(8)
    assert is_balanced(root) == False


def test_balanced_left_heavy():
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    assert is_balanced(root) == True


def test_balanced_right_heavy():
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.right.left = Node(4)
    root.right.right = Node(5)
    assert is_balanced(root) == True


def test_unbalanced_left_subtree():
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    root.left.left.left = Node(6)
    root.left.left.right = Node(7)
    root.left.right.left = Node(8)
    assert is_balanced(root) == False


def test_unbalanced_right_subtree():
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.right.left = Node(4)
    root.right.right = Node(5)
    root.right.left.left = Node(6)
    root.right.left.right = Node(7)
    root.right.right.right = Node(8)
    assert is_balanced(root) == False


def test_balanced_complete_tree():
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    root.right.left = Node(6)
    assert is_balanced(root) == True


def test_unbalanced_large_tree():
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    root.right.right = Node(6)
    root.left.left.left = Node(7)
    root.left.left.right = Node(8)
    root.left.right.left = Node(9)
    root.left.right.right = Node(10)
    root.left.left.left.left = Node(11)
    assert is_balanced(root) == False


def test_balanced_three_levels():
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    root.right.left = Node(6)
    root.right.right = Node(7)
    root.left.left.left = Node(8)
    assert is_balanced(root) == True


def test_unbalanced_only_left():
    root = Node(1)
    current = root
    for i in range(2, 6):
        current.left = Node(i)
        current = current.left
    assert is_balanced(root) == False


def test_unbalanced_only_right():
    root = Node(1)
    current = root
    for i in range(2, 6):
        current.right = Node(i)
        current = current.right
    assert is_balanced(root) == False


def test_balanced_sparse():
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.right.left = Node(4)
    assert is_balanced(root) == True


def test_balanced_zigzag_deep():
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.right = Node(4)
    root.right.left = Node(5)
    root.left.right.left = Node(6)
    root.right.left.right = Node(7)
    assert is_balanced(root) == False


def test_unbalanced_zigzag_broken():
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.right = Node(4)
    root.right.left = Node(5)
    root.left.right.left = Node(6)
    root.left.right.left.left = Node(7)
    assert is_balanced(root) == False

