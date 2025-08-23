# ESSENTIAL ALGORITHMS FOR LEAPFROG EXAM
# These are the most commonly asked algorithm implementations

# =============================================================================
# 1. LINEAR SEARCH - O(n)
# =============================================================================
def linear_search(arr, target):
    """
    Search for target in array sequentially
    Time Complexity: O(n) - worst case check every element
    Space Complexity: O(1) - no extra space needed
    
    Example: linear_search([3, 1, 4, 2, 5], 4) -> 2 (index where 4 is found)
    """
    for i in range(len(arr)):
        if arr[i] == target:
            return i  # Return index if found
    return -1  # Return -1 if not found


# Test Linear Search
print("=== LINEAR SEARCH ===")
test_arr = [3, 1, 4, 2, 5]
print(f"Array: {test_arr}")
print(f"Search for 4: index {linear_search(test_arr, 4)}")  # Should return 2
print(f"Search for 6: index {linear_search(test_arr, 6)}")  # Should return -1
