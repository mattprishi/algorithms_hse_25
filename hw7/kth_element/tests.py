import pytest
import os


solution_module = int(os.getenv('SOLUTION', '1'))

if solution_module == 2:
    from solution_2 import find_kth_largest
else:
    from solution_1 import find_kth_largest, MinHeap
    solution_module = 1


def test_example_1():
    nums = [3, 2, 1, 5, 6, 4]
    k = 2
    assert find_kth_largest(nums, k) == 5


def test_example_2():
    nums = [3, 2, 3, 1, 2, 4, 5, 5, 6]
    k = 4
    assert find_kth_largest(nums, k) == 4


def test_kth_largest_basic():
    assert find_kth_largest([1, 2, 3, 4, 5], 1) == 5
    assert find_kth_largest([1, 2, 3, 4, 5], 2) == 4
    assert find_kth_largest([1, 2, 3, 4, 5], 3) == 3
    assert find_kth_largest([1, 2, 3, 4, 5], 5) == 1


def test_single_element():
    assert find_kth_largest([1], 1) == 1


def test_two_elements():
    assert find_kth_largest([2, 1], 1) == 2
    assert find_kth_largest([2, 1], 2) == 1


def test_duplicates():
    assert find_kth_largest([1, 1, 1, 1], 1) == 1
    assert find_kth_largest([1, 1, 1, 1], 2) == 1
    assert find_kth_largest([5, 2, 2, 5, 3], 2) == 5


def test_negative_numbers():
    assert find_kth_largest([-1, -2, -3, -4, -5], 1) == -1
    assert find_kth_largest([-1, -2, -3, -4, -5], 3) == -3
    assert find_kth_largest([3, -1, 2, -5, 4], 2) == 3


def test_large_array():
    nums = list(range(1, 1001))
    assert find_kth_largest(nums, 1) == 1000
    assert find_kth_largest(nums, 10) == 991
    assert find_kth_largest(nums, 500) == 501


def test_reverse_sorted():
    nums = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
    assert find_kth_largest(nums, 1) == 10
    assert find_kth_largest(nums, 5) == 6


def test_edge_cases():
    assert find_kth_largest([], 1) is None
    assert find_kth_largest([1, 2, 3], 0) is None
    assert find_kth_largest([1, 2, 3], 4) is None
    assert find_kth_largest([1, 2, 3], -1) is None


def test_unsorted_array():
    nums = [7, 10, 4, 3, 20, 15]
    assert find_kth_largest(nums, 1) == 20
    assert find_kth_largest(nums, 2) == 15
    assert find_kth_largest(nums, 3) == 10
    assert find_kth_largest(nums, 4) == 7


def test_all_equal():
    assert find_kth_largest([5, 5, 5, 5, 5], 1) == 5
    assert find_kth_largest([5, 5, 5, 5, 5], 3) == 5
    assert find_kth_largest([5, 5, 5, 5, 5], 5) == 5


@pytest.mark.skipif(solution_module != 1, reason="MinHeap only in solution_1")
def test_minheap_push_pop():
    heap = MinHeap()
    heap.push(5)
    heap.push(3)
    heap.push(7)
    heap.push(1)
    
    assert heap.peek() == 1
    assert heap.pop() == 1
    assert heap.peek() == 3
    assert heap.pop() == 3
    assert heap.peek() == 5


@pytest.mark.skipif(solution_module != 1, reason="MinHeap only in solution_1")
def test_minheap_empty():
    heap = MinHeap()
    assert heap.peek() is None
    assert heap.pop() is None
    assert heap.size() == 0


@pytest.mark.skipif(solution_module != 1, reason="MinHeap only in solution_1")
def test_minheap_single():
    heap = MinHeap()
    heap.push(42)
    assert heap.peek() == 42
    assert heap.size() == 1
    assert heap.pop() == 42
    assert heap.size() == 0


@pytest.mark.skipif(solution_module != 1, reason="MinHeap only in solution_1")
def test_minheap_duplicates():
    heap = MinHeap()
    for val in [5, 5, 3, 3, 7, 7]:
        heap.push(val)
    
    assert heap.pop() == 3
    assert heap.pop() == 3
    assert heap.pop() == 5
    assert heap.pop() == 5


@pytest.mark.skipif(solution_module != 1, reason="MinHeap only in solution_1")
def test_minheap_maintains_property():
    heap = MinHeap()
    values = [10, 5, 15, 3, 7, 12, 20]
    
    for val in values:
        heap.push(val)
    
    result = []
    while heap.size() > 0:
        result.append(heap.pop())
    
    assert result == sorted(values)


def test_does_not_modify_original():
    original = [3, 1, 4, 1, 5]
    original_copy = original.copy()
    find_kth_largest(original, 2)
    assert original == original_copy


def test_random_arrays():
    import random
    random.seed(42)
    
    for _ in range(10):
        nums = [random.randint(-100, 100) for _ in range(20)]
        k = random.randint(1, 20)
        result = find_kth_largest(nums, k)
        expected = sorted(nums, reverse=True)[k - 1]
        assert result == expected


def test_performance_comparison():
    import time
    import random
    
    random.seed(42)
    nums = [random.randint(-10000, 10000) for _ in range(5000)]
    k = 100
    
    start = time.perf_counter()
    result = find_kth_largest(nums.copy(), k)
    elapsed = time.perf_counter() - start
    
    expected = sorted(nums, reverse=True)[k - 1]
    
    print(f"\n[Performance test n=5000, k={k}]")
    print(f"  Time: {elapsed:.6f}s")
    print(f"  Result: {result}")
    print(f"  Expected: {expected}")
    
    assert result == expected

