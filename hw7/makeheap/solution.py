import time
from functools import wraps


def timer(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        result = func(*args, **kwargs)
        end = time.perf_counter()
        elapsed = end - start
        return result, elapsed
    return wrapper


def heapify_up(arr, index):
    while index > 0:
        parent = (index - 1) // 2
        if arr[index] < arr[parent]:
            arr[index], arr[parent] = arr[parent], arr[index]
            index = parent
        else:
            break


def heapify_down(arr, n, index):
    smallest = index
    left = 2 * index + 1
    right = 2 * index + 2
    
    if left < n and arr[left] < arr[smallest]:
        smallest = left
    
    if right < n and arr[right] < arr[smallest]:
        smallest = right
    
    if smallest != index:
        arr[index], arr[smallest] = arr[smallest], arr[index]
        heapify_down(arr, n, smallest)


def makeheap_n_log_n(arr):
    if not arr:
        return []
    
    result = []
    for element in arr:
        result.append(element)
        heapify_up(result, len(result) - 1)
    
    return result


def makeheap(arr):
    if not arr:
        return []
    
    result = arr.copy()
    n = len(result)
    
    for i in range(n // 2 - 1, -1, -1):
        heapify_down(result, n, i)
    
    return result

