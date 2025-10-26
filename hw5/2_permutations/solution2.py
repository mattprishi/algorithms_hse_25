import sys
sys.path.append('../1_tracer')
from solution1 import tracer


def permutations(nums):
    results = []
    
    @tracer
    def find_permutations_recursive(current_permutation, available_nums):
        if not available_nums:
            results.append(current_permutation)
            return
        
        for i, num in enumerate(available_nums):
            new_permutation = current_permutation + [num]
            new_available = available_nums[:i] + available_nums[i+1:]
            find_permutations_recursive(new_permutation, new_available)
    
    find_permutations_recursive([], nums)
    return results

# if __name__ == "__main__":
#     nums = [1, 2, 3]
#     result = permutations(nums)
#     print(result)