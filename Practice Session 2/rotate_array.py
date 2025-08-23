# =============================================================================
# PROBLEM 6: ARRAY ROTATION (Medium)
# =============================================================================
def rotate_array(arr, k):
    """
    Rotate array to the right by k steps
    Example: [1,2,3,4,5], k=2 -> [4,5,1,2,3]
    """
    if not arr or k == 0:
        return arr

    n = len(arr)
    k = k % n  # Handle k > n
    return arr[-k:] + arr[:-k]


# Test cases
print("\nProblem 6 - Rotate Array:")
print(rotate_array([1, 2, 3, 4, 5], 2))      # Should output: [4,5,1,2,3]
print(rotate_array([1, 2], 3))            # Should output: [2,1]
print(rotate_array([1], 1))              # Should output: [1]
