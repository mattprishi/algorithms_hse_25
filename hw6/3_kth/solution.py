def find_kth_largest(nums, k):
    def partition(left, right):
        pivot = nums[right]
        i = left - 1
        
        for j in range(left, right):
            if nums[j] <= pivot:
                i += 1
                nums[i], nums[j] = nums[j], nums[i]
        
        nums[i + 1], nums[right] = nums[right], nums[i + 1]
        return i + 1
    
    def quickselect(left, right, target_idx):
        if left == right:
            return nums[left]
        
        pivot_idx = partition(left, right)
        
        if pivot_idx == target_idx:
            return nums[pivot_idx]
        elif pivot_idx < target_idx:
            return quickselect(pivot_idx + 1, right, target_idx)
        else:
            return quickselect(left, pivot_idx - 1, target_idx)
    
    nums = nums.copy()
    n = len(nums)
    target_idx = n - k
    
    return quickselect(0, n - 1, target_idx)

