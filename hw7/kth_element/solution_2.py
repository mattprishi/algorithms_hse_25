# Решение с использованием heapq

import heapq


def find_kth_largest(nums, k):
    if not nums or k <= 0 or k > len(nums):
        return None
    
    heap = []
    
    for num in nums:
        heapq.heappush(heap, num)
        if len(heap) > k:
            heapq.heappop(heap)
    
    return heap[0]

