# (из 1_2_merge_quick) SOLUTION=2 python3 -m pytest tests.py -v -s

def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    
    arr = arr.copy()
    width = 1
    n = len(arr)
    
    while width < n:
        for i in range(0, n, width * 2):
            left = i
            mid = min(i + width, n)
            right = min(i + width * 2, n)
            
            merge_in_place(arr, left, mid, right)
        
        width *= 2
    
    return arr


def merge_in_place(arr, left, mid, right):
    left_part = arr[left:mid]
    right_part = arr[mid:right]
    
    i = j = 0
    k = left
    
    while i < len(left_part) and j < len(right_part):
        if left_part[i] <= right_part[j]:
            arr[k] = left_part[i]
            i += 1
        else:
            arr[k] = right_part[j]
            j += 1
        k += 1
    
    while i < len(left_part):
        arr[k] = left_part[i]
        i += 1
        k += 1
    
    while j < len(right_part):
        arr[k] = right_part[j]
        j += 1
        k += 1


def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    
    arr = arr.copy()
    stack = [(0, len(arr) - 1)]
    
    while stack:
        low, high = stack.pop()
        
        if low < high:
            pivot_idx = partition(arr, low, high)
            
            stack.append((low, pivot_idx - 1))
            stack.append((pivot_idx + 1, high))
    
    return arr


def partition(arr, low, high):
    pivot = arr[high]
    i = low - 1
    
    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1


