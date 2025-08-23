# =============================================================================
# PROBLEM 3: ARRAY SEARCH (Medium)
# =============================================================================
def two_sum(nums, target):
    """
    Find two numbers in array that add up to target
    Return their indices
    Example: [2, 7, 11, 15], target=9 -> [0, 1] (because 2+7=9)
    """
    seen = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in seen:
            return [seen[complement], i]
        seen[num] = i
    return []


# Test cases
print("\nProblem 3 - Two Sum:")
print(two_sum([2, 7, 11, 15], 9))     # Should output: [0, 1]
print(two_sum([3, 2, 4], 6))          # Should output: [1, 2]
print(two_sum([3, 3], 6))             # Should output: [0, 1]
