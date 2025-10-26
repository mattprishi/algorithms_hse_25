import pytest
from solution import BST


@pytest.fixture
def balanced_tree():
    bst = BST()
    values = [10, 5, 15, 3, 7, 12, 20]
    for val in values:
        bst.insert(val)
    return bst


@pytest.fixture
def complex_tree():
    bst = BST()
    values = [50, 30, 70, 20, 40, 60, 80, 10, 25, 35, 45]
    for val in values:
        bst.insert(val)
    return bst


def test_empty_tree():
    bst = BST()
    assert bst.pre_order() == []
    assert bst.in_order() == []
    assert bst.post_order() == []
    assert bst.reverse_pre_order() == []
    assert bst.reverse_in_order() == []
    assert bst.reverse_post_order() == []


def test_single_node():
    bst = BST()
    bst.insert(10)
    assert bst.pre_order() == [10]
    assert bst.in_order() == [10]
    assert bst.post_order() == [10]
    assert bst.reverse_pre_order() == [10]
    assert bst.reverse_in_order() == [10]
    assert bst.reverse_post_order() == [10]


def test_balanced_tree(balanced_tree):
    assert balanced_tree.pre_order() == [10, 5, 3, 7, 15, 12, 20]
    assert balanced_tree.in_order() == [3, 5, 7, 10, 12, 15, 20]
    assert balanced_tree.post_order() == [3, 7, 5, 12, 20, 15, 10]
    assert balanced_tree.reverse_pre_order() == [10, 15, 20, 12, 5, 7, 3]
    assert balanced_tree.reverse_in_order() == [20, 15, 12, 10, 7, 5, 3]
    assert balanced_tree.reverse_post_order() == [20, 12, 15, 7, 3, 5, 10]


def test_left_skewed_tree():
    bst = BST()
    for val in [10, 8, 6, 4, 2]:
        bst.insert(val)
    
    assert bst.pre_order() == [10, 8, 6, 4, 2]
    assert bst.in_order() == [2, 4, 6, 8, 10]
    assert bst.post_order() == [2, 4, 6, 8, 10]
    assert bst.reverse_pre_order() == [10, 8, 6, 4, 2]
    assert bst.reverse_in_order() == [10, 8, 6, 4, 2]
    assert bst.reverse_post_order() == [2, 4, 6, 8, 10]


def test_right_skewed_tree():
    bst = BST()
    for val in [2, 4, 6, 8, 10]:
        bst.insert(val)
    
    assert bst.pre_order() == [2, 4, 6, 8, 10]
    assert bst.in_order() == [2, 4, 6, 8, 10]
    assert bst.post_order() == [10, 8, 6, 4, 2]
    assert bst.reverse_pre_order() == [2, 4, 6, 8, 10]
    assert bst.reverse_in_order() == [10, 8, 6, 4, 2]
    assert bst.reverse_post_order() == [10, 8, 6, 4, 2]


def test_complex_tree(complex_tree):
    assert complex_tree.pre_order() == [50, 30, 20, 10, 25, 40, 35, 45, 70, 60, 80]
    assert complex_tree.in_order() == [10, 20, 25, 30, 35, 40, 45, 50, 60, 70, 80]
    assert complex_tree.post_order() == [10, 25, 20, 35, 45, 40, 30, 60, 80, 70, 50]
    assert complex_tree.reverse_pre_order() == [50, 70, 80, 60, 30, 40, 45, 35, 20, 25, 10]
    assert complex_tree.reverse_in_order() == [80, 70, 60, 50, 45, 40, 35, 30, 25, 20, 10]
    assert complex_tree.reverse_post_order() == [80, 60, 70, 45, 35, 40, 25, 10, 20, 30, 50]


def test_duplicate_values():
    bst = BST()
    bst.insert(10)
    bst.insert(10)
    bst.insert(5)
    bst.insert(5)
    
    assert bst.pre_order() == [10, 5, 5, 10]
    assert bst.in_order() == [5, 5, 10, 10]
    assert bst.post_order() == [5, 5, 10, 10]
    assert bst.reverse_pre_order() == [10, 10, 5, 5]
    assert bst.reverse_in_order() == [10, 10, 5, 5]
    assert bst.reverse_post_order() == [10, 5, 5, 10]


def test_property_reverse_in_order(balanced_tree):
    assert balanced_tree.reverse_in_order() == list(reversed(balanced_tree.in_order()))


def test_property_reverse_in_order_complex(complex_tree):
    assert complex_tree.reverse_in_order() == list(reversed(complex_tree.in_order()))


def test_string_data():
    bst = BST()
    for char in ['f', 'b', 'g', 'a', 'd', 'c', 'e']:
        bst.insert(char)
    
    assert bst.in_order() == ['a', 'b', 'c', 'd', 'e', 'f', 'g']
    assert bst.reverse_in_order() == ['g', 'f', 'e', 'd', 'c', 'b', 'a']
    assert bst.pre_order() == ['f', 'b', 'a', 'd', 'c', 'e', 'g']

