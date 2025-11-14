import pytest
import random


from solution import makeheap_n_log_n, makeheap, timer


def is_min_heap(arr):
    n = len(arr)
    for i in range(n):
        left = 2 * i + 1
        right = 2 * i + 2
        
        if left < n and arr[i] > arr[left]:
            return False
        if right < n and arr[i] > arr[right]:
            return False
    
    return True


def test_makeheap_n_log_n_basic():
    arr = [3, 1, 4, 1, 5, 9, 2, 6]
    result = makeheap_n_log_n(arr)
    assert is_min_heap(result)
    assert sorted(result) == sorted(arr)


def test_makeheap_basic():
    arr = [3, 1, 4, 1, 5, 9, 2, 6]
    result = makeheap(arr)
    assert is_min_heap(result)
    assert sorted(result) == sorted(arr)


@pytest.mark.parametrize("heap_func", [makeheap_n_log_n, makeheap])
def test_empty_array(heap_func):
    assert heap_func([]) == []


@pytest.mark.parametrize("heap_func", [makeheap_n_log_n, makeheap])
def test_single_element(heap_func):
    arr = [5]
    result = heap_func(arr)
    assert result == [5]
    assert is_min_heap(result)


@pytest.mark.parametrize("heap_func", [makeheap_n_log_n, makeheap])
def test_two_elements(heap_func):
    arr = [2, 1]
    result = heap_func(arr)
    assert is_min_heap(result)
    assert sorted(result) == [1, 2]


@pytest.mark.parametrize("heap_func", [makeheap_n_log_n, makeheap])
def test_already_heap(heap_func):
    arr = [1, 2, 3, 4, 5]
    result = heap_func(arr)
    assert is_min_heap(result)
    assert sorted(result) == sorted(arr)


@pytest.mark.parametrize("heap_func", [makeheap_n_log_n, makeheap])
def test_reverse_sorted(heap_func):
    arr = [5, 4, 3, 2, 1]
    result = heap_func(arr)
    assert is_min_heap(result)
    assert sorted(result) == [1, 2, 3, 4, 5]


@pytest.mark.parametrize("heap_func", [makeheap_n_log_n, makeheap])
def test_duplicates(heap_func):
    arr = [5, 2, 3, 2, 1, 5]
    result = heap_func(arr)
    assert is_min_heap(result)
    assert sorted(result) == sorted(arr)


@pytest.mark.parametrize("heap_func", [makeheap_n_log_n, makeheap])
def test_all_same(heap_func):
    arr = [7, 7, 7, 7, 7]
    result = heap_func(arr)
    assert is_min_heap(result)
    assert result == arr


@pytest.mark.parametrize("heap_func", [makeheap_n_log_n, makeheap])
def test_negative_numbers(heap_func):
    arr = [-5, -1, -3, 0, 2]
    result = heap_func(arr)
    assert is_min_heap(result)
    assert sorted(result) == [-5, -3, -1, 0, 2]


@pytest.mark.parametrize("heap_func", [makeheap_n_log_n, makeheap])
def test_large_array(heap_func):
    arr = list(range(1000, 0, -1))
    result = heap_func(arr)
    assert is_min_heap(result)
    assert sorted(result) == list(range(1, 1001))


@pytest.mark.parametrize("heap_func", [makeheap_n_log_n, makeheap])
def test_does_not_modify_original(heap_func):
    original = [3, 1, 4, 1, 5]
    original_copy = original.copy()
    heap_func(original)
    assert original == original_copy


def test_timer_decorator():
    @timer
    def sample_func(n):
        return sum(range(n))
    
    result, elapsed = sample_func(1000)
    assert result == sum(range(1000))
    assert elapsed > 0


def test_performance_comparison_small():
    arr = list(range(100, 0, -1))
    
    @timer
    def test_n_log_n(arr):
        return makeheap_n_log_n(arr)
    
    @timer
    def test_n(arr):
        return makeheap(arr)
    
    result_nlogn, time_nlogn = test_n_log_n(arr.copy())
    result_n, time_n = test_n(arr.copy())
    
    print(f"\n[Small array n=100]")
    print(f"  makeheap_n_log_n: {time_nlogn:.6f}s")
    print(f"  makeheap: {time_n:.6f}s")
    print(f"  Ratio (O(N log N) / O(N)): {time_nlogn/time_n:.2f}x")
    
    assert is_min_heap(result_nlogn)
    assert is_min_heap(result_n)


def test_performance_comparison_medium():
    arr = list(range(1000, 0, -1))
    
    @timer
    def test_n_log_n(arr):
        return makeheap_n_log_n(arr)
    
    @timer
    def test_n(arr):
        return makeheap(arr)
    
    result_nlogn, time_nlogn = test_n_log_n(arr.copy())
    result_n, time_n = test_n(arr.copy())
    
    print(f"\n[Medium array n=1000]")
    print(f"  makeheap_n_log_n: {time_nlogn:.6f}s")
    print(f"  makeheap: {time_n:.6f}s")
    print(f"  Ratio (O(N log N) / O(N)): {time_nlogn/time_n:.2f}x")
    
    assert is_min_heap(result_nlogn)
    assert is_min_heap(result_n)


def test_performance_comparison_large():
    arr = list(range(10000, 0, -1))
    
    @timer
    def test_n_log_n(arr):
        return makeheap_n_log_n(arr)
    
    @timer
    def test_n(arr):
        return makeheap(arr)
    
    result_nlogn, time_nlogn = test_n_log_n(arr.copy())
    result_n, time_n = test_n(arr.copy())
    
    print(f"\n[Large array n=10000]")
    print(f"  makeheap_n_log_n: {time_nlogn:.6f}s")
    print(f"  makeheap: {time_n:.6f}s")
    print(f"  Ratio (O(N log N) / O(N)): {time_nlogn/time_n:.2f}x")
    
    assert is_min_heap(result_nlogn)
    assert is_min_heap(result_n)


def test_performance_comparison_random():
    random.seed(42)
    arr = [random.randint(-1000, 1000) for _ in range(5000)]
    
    @timer
    def test_n_log_n(arr):
        return makeheap_n_log_n(arr)
    
    @timer
    def test_n(arr):
        return makeheap(arr)
    
    result_nlogn, time_nlogn = test_n_log_n(arr.copy())
    result_n, time_n = test_n(arr.copy())
    
    print(f"\n[Random array n=5000]")
    print(f"  makeheap_n_log_n: {time_nlogn:.6f}s")
    print(f"  makeheap: {time_n:.6f}s")
    print(f"  Ratio (O(N log N) / O(N)): {time_nlogn/time_n:.2f}x")
    
    assert is_min_heap(result_nlogn)
    assert is_min_heap(result_n)

