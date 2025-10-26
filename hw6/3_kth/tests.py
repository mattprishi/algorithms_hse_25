import pytest
from solution import find_kth_largest


def test_example_1():
    nums = [3, 2, 1, 5, 6, 4]
    k = 2
    assert find_kth_largest(nums, k) == 5


def test_example_2():
    nums = [3, 2, 3, 1, 2, 4, 5, 5, 6]
    k = 4
    assert find_kth_largest(nums, k) == 4


def test_single_element():
    assert find_kth_largest([1], 1) == 1


def test_largest_element():
    nums = [3, 2, 1, 5, 6, 4]
    k = 1
    assert find_kth_largest(nums, k) == 6


def test_smallest_as_kth_largest():
    nums = [3, 2, 1, 5, 6, 4]
    k = 6
    assert find_kth_largest(nums, k) == 1


def test_duplicates():
    nums = [5, 5, 5, 5, 5]
    k = 3
    assert find_kth_largest(nums, k) == 5


def test_two_elements():
    assert find_kth_largest([1, 2], 1) == 2
    assert find_kth_largest([1, 2], 2) == 1


def test_negative_numbers():
    nums = [-5, -1, -3, 0, 2]
    k = 2
    assert find_kth_largest(nums, k) == 0


def test_all_negative():
    nums = [-1, -2, -3, -4]
    k = 2
    assert find_kth_largest(nums, k) == -2


def test_mixed_duplicates():
    nums = [3, 2, 3, 1, 2, 4, 5, 5, 6]
    k = 1
    assert find_kth_largest(nums, k) == 6


def test_large_array():
    nums = list(range(1000))
    k = 500
    assert find_kth_largest(nums, k) == 1000 - k


def test_does_not_modify_original():
    original = [3, 2, 1, 5, 6, 4]
    original_copy = original.copy()
    find_kth_largest(original, 2)
    assert original == original_copy

