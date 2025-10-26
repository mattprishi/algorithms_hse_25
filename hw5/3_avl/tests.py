import pytest
from solution import AVL


def test_insert_single_element():
    avl = AVL()
    avl.insert(10)
    assert avl.search(10) is True
    assert avl.root.key == 10
    assert avl.root.height == 1


def test_insert_multiple_elements():
    avl = AVL()
    elements = [10, 20, 30, 40, 50, 25]
    for elem in elements:
        avl.insert(elem)
    
    for elem in elements:
        assert avl.search(elem) is True


def test_search_existing_element():
    avl = AVL()
    avl.insert(10)
    avl.insert(5)
    avl.insert(15)
    
    assert avl.search(10) is True
    assert avl.search(5) is True
    assert avl.search(15) is True


def test_search_non_existing_element():
    avl = AVL()
    avl.insert(10)
    avl.insert(5)
    avl.insert(15)
    
    assert avl.search(100) is False
    assert avl.search(3) is False


def test_search_empty_tree():
    avl = AVL()
    assert avl.search(10) is False


def test_delete_leaf():
    avl = AVL()
    avl.insert(10)
    avl.insert(5)
    avl.insert(15)
    
    avl.delete(5)
    assert avl.search(5) is False
    assert avl.search(10) is True
    assert avl.search(15) is True


def test_delete_node_with_one_child():
    avl = AVL()
    avl.insert(10)
    avl.insert(5)
    avl.insert(15)
    avl.insert(20)
    
    avl.delete(15)
    assert avl.search(15) is False
    assert avl.search(20) is True


def test_delete_node_with_two_children():
    avl = AVL()
    avl.insert(10)
    avl.insert(5)
    avl.insert(15)
    avl.insert(12)
    avl.insert(20)
    
    avl.delete(15)
    assert avl.search(15) is False
    assert avl.search(20) is True
    assert avl.search(12) is True


def test_delete_root():
    avl = AVL()
    avl.insert(10)
    avl.insert(5)
    avl.insert(15)
    
    avl.delete(10)
    assert avl.search(10) is False
    assert avl.search(5) is True
    assert avl.search(15) is True


def test_delete_non_existing():
    avl = AVL()
    avl.insert(10)
    avl.delete(100)
    assert avl.search(10) is True


def test_right_rotation():
    avl = AVL()
    avl.insert(30)
    avl.insert(20)
    avl.insert(10)
    
    assert avl.root.key == 20
    assert avl.root.left.key == 10
    assert avl.root.right.key == 30
    assert avl.is_balanced()


def test_left_rotation():
    avl = AVL()
    avl.insert(10)
    avl.insert(20)
    avl.insert(30)
    
    assert avl.root.key == 20
    assert avl.root.left.key == 10
    assert avl.root.right.key == 30
    assert avl.is_balanced()


def test_left_right_rotation():
    avl = AVL()
    avl.insert(30)
    avl.insert(10)
    avl.insert(20)
    
    assert avl.root.key == 20
    assert avl.root.left.key == 10
    assert avl.root.right.key == 30
    assert avl.is_balanced()


def test_right_left_rotation():
    avl = AVL()
    avl.insert(10)
    avl.insert(30)
    avl.insert(20)
    
    assert avl.root.key == 20
    assert avl.root.left.key == 10
    assert avl.root.right.key == 30
    assert avl.is_balanced()


def test_balance_after_multiple_inserts():
    avl = AVL()
    elements = [10, 20, 30, 40, 50, 25]
    for elem in elements:
        avl.insert(elem)
    
    assert avl.is_balanced()


def test_balance_after_deletions():
    avl = AVL()
    elements = [10, 20, 30, 40, 50, 25]
    for elem in elements:
        avl.insert(elem)
    
    avl.delete(10)
    assert avl.is_balanced()
    
    avl.delete(50)
    assert avl.is_balanced()


def test_inorder_traversal():
    avl = AVL()
    elements = [30, 20, 40, 10, 25, 35, 50]
    for elem in elements:
        avl.insert(elem)
    
    inorder = avl.inorder()
    assert inorder == sorted(elements)


def test_large_tree():
    avl = AVL()
    elements = list(range(1, 101))
    
    for elem in elements:
        avl.insert(elem)
    
    assert avl.is_balanced()
    
    for elem in elements:
        assert avl.search(elem) is True


def test_delete_all_elements():
    avl = AVL()
    elements = [10, 20, 30, 40, 50]
    
    for elem in elements:
        avl.insert(elem)
    
    for elem in elements:
        avl.delete(elem)
        assert avl.search(elem) is False
    
    assert avl.root is None


def test_insert_duplicates():
    avl = AVL()
    avl.insert(10)
    avl.insert(10)
    
    assert avl.search(10) is True
    inorder = avl.inorder()
    assert inorder.count(10) == 1


def test_height_calculation():
    avl = AVL()
    avl.insert(10)
    assert avl.root.height == 1
    
    avl.insert(5)
    avl.insert(15)
    assert avl.root.height == 2


def test_complex_scenario():
    avl = AVL()
    
    for i in [50, 25, 75, 10, 30, 60, 80, 5, 15, 27, 55, 1]:
        avl.insert(i)
    
    assert avl.is_balanced()
    
    avl.delete(1)
    assert avl.is_balanced()
    
    avl.delete(10)
    assert avl.is_balanced()
    
    avl.delete(5)
    assert avl.is_balanced()
    
    assert avl.search(50) is True
    assert avl.search(1) is False

