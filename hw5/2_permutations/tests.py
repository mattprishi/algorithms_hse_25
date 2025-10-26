import pytest
from solution2 import permutations


def test_three_elements():
    nums = [1, 2, 3]
    result = permutations(nums)
    expected = [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]]
    assert len(result) == len(expected)
    assert sorted(result) == sorted(expected)


def test_two_elements():
    nums = [0, 1]
    result = permutations(nums)
    expected = [[0, 1], [1, 0]]
    assert len(result) == len(expected)
    assert sorted(result) == sorted(expected)


def test_single_element():
    nums = [1]
    result = permutations(nums)
    expected = [[1]]
    assert result == expected


def test_empty_array():
    nums = []
    result = permutations(nums)
    expected = [[]]
    assert result == expected


def test_four_elements():
    nums = [1, 2, 3, 4]
    result = permutations(nums)
    assert len(result) == 24
    assert len(set(tuple(p) for p in result)) == 24


def test_with_duplicates():
    nums = [1, 1, 2]
    result = permutations(nums)
    assert len(result) == 6


def test_negative_numbers():
    nums = [-1, 0, 1]
    result = permutations(nums)
    assert len(result) == 6
    assert [-1, 0, 1] in result
    assert [1, 0, -1] in result


def test_all_permutations_different():
    nums = [1, 2, 3]
    result = permutations(nums)
    unique_perms = [tuple(p) for p in result]
    assert len(unique_perms) == len(set(unique_perms))

