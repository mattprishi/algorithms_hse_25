import pytest
import os


solution_module = int(os.getenv('SOLUTION', '1'))

if solution_module == 2:
    from solution_2 import merge_sort, quick_sort
else:
    from solution_1 import merge_sort, quick_sort, timer
    solution_module = 1


ALL_SORTS = [merge_sort, quick_sort]


@pytest.mark.parametrize("sort_func", ALL_SORTS)
def test_sort_basic(sort_func):
    assert sort_func([3, 1, 4, 1, 5, 9, 2, 6]) == [1, 1, 2, 3, 4, 5, 6, 9]
    assert sort_func([5, 4, 3, 2, 1]) == [1, 2, 3, 4, 5]
    assert sort_func([1]) == [1]
    assert sort_func([]) == []


@pytest.mark.parametrize("sort_func", ALL_SORTS)
def test_sort_duplicates(sort_func):
    assert sort_func([5, 2, 3, 2, 1, 5]) == [1, 2, 2, 3, 5, 5]
    assert sort_func([1, 1, 1, 1]) == [1, 1, 1, 1]


@pytest.mark.parametrize("sort_func", ALL_SORTS)
def test_sort_large(sort_func):
    arr = list(range(1000, 0, -1))
    sorted_arr = list(range(1, 1001))
    assert sort_func(arr) == sorted_arr


@pytest.mark.parametrize("sort_func", ALL_SORTS)
def test_sort_negative(sort_func):
    assert sort_func([-5, -1, -3, 0, 2]) == [-5, -3, -1, 0, 2]


@pytest.mark.parametrize("sort_func", ALL_SORTS)
def test_sort_already_sorted(sort_func):
    arr = [1, 2, 3, 4, 5]
    assert sort_func(arr) == arr


def test_merge_sort_does_not_modify_original():
    original = [3, 1, 4, 1, 5]
    original_copy = original.copy()
    merge_sort(original)
    assert original == original_copy


def test_quick_sort_does_not_modify_original():
    original = [3, 1, 4, 1, 5]
    original_copy = original.copy()
    quick_sort(original)
    assert original == original_copy


@pytest.mark.parametrize("sort_func", ALL_SORTS)
def test_sort_two_elements(sort_func):
    assert sort_func([2, 1]) == [1, 2]
    assert sort_func([1, 2]) == [1, 2]


@pytest.mark.skipif(solution_module != 1, reason="Timer only in solution_1")
def test_timer_decorator():
    @timer
    def sample_func(n):
        return sum(range(n))
    
    result, elapsed = sample_func(1000)
    assert result == sum(range(1000))
    assert elapsed > 0


@pytest.mark.skipif(solution_module != 1, reason="Performance tests only for solution_1")
def test_sorted_array_timing():
    sorted_arr = list(range(1000))
    
    @timer
    def merge_timed(arr):
        return merge_sort(arr)
    
    @timer
    def quick_timed(arr):
        return quick_sort(arr)
    
    merge_result, merge_time = merge_timed(sorted_arr.copy())
    quick_result, quick_time = quick_timed(sorted_arr.copy())
    
    print(f"\n[Sorted array n=1000]")
    print(f"  Merge sort: {merge_time:.6f}s")
    print(f"  Quick sort: {quick_time:.6f}s")
    print(f"  Ratio (quick/merge): {quick_time/merge_time:.2f}x")
    
    assert merge_result == sorted_arr
    assert quick_result == sorted_arr


@pytest.mark.skipif(solution_module != 1, reason="Performance tests only for solution_1")
def test_reverse_sorted_timing():
    reverse_arr = list(range(1000, 0, -1))
    expected = list(range(1, 1001))
    
    @timer
    def merge_timed(arr):
        return merge_sort(arr)
    
    @timer
    def quick_timed(arr):
        return quick_sort(arr)
    
    merge_result, merge_time = merge_timed(reverse_arr.copy())
    quick_result, quick_time = quick_timed(reverse_arr.copy())
    
    print(f"\n[Reverse sorted array n=1000]")
    print(f"  Merge sort: {merge_time:.6f}s")
    print(f"  Quick sort: {quick_time:.6f}s")
    print(f"  Ratio (quick/merge): {quick_time/merge_time:.2f}x")
    
    assert merge_result == expected
    assert quick_result == expected


@pytest.mark.skipif(solution_module != 1, reason="Performance tests only for solution_1")
def test_all_duplicates_timing():
    dup_arr = [5] * 1000
    
    @timer
    def merge_timed(arr):
        return merge_sort(arr)
    
    @timer
    def quick_timed(arr):
        return quick_sort(arr)
    
    merge_result, merge_time = merge_timed(dup_arr.copy())
    quick_result, quick_time = quick_timed(dup_arr.copy())
    
    print(f"\n[All duplicates n=1000]")
    print(f"  Merge sort: {merge_time:.6f}s")
    print(f"  Quick sort: {quick_time:.6f}s")
    print(f"  Ratio (quick/merge): {quick_time/merge_time:.2f}x")
    
    assert merge_result == dup_arr
    assert quick_result == dup_arr


@pytest.mark.skipif(solution_module != 1, reason="Performance tests only for solution_1")
def test_random_array_timing():
    import random
    
    random_arr = list(range(2000))
    random.shuffle(random_arr)
    expected = list(range(2000))
    
    @timer
    def merge_timed(arr):
        return merge_sort(arr)
    
    @timer
    def quick_timed(arr):
        return quick_sort(arr)
    
    merge_result, merge_time = merge_timed(random_arr.copy())
    quick_result, quick_time = quick_timed(random_arr.copy())
    
    print(f"\n[Random array n=2000]")
    print(f"  Merge sort: {merge_time:.6f}s")
    print(f"  Quick sort: {quick_time:.6f}s")
    print(f"  Ratio (quick/merge): {quick_time/merge_time:.2f}x")
    
    assert merge_result == expected
    assert quick_result == expected

