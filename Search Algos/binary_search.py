# =============================================================================
# 2. BINARY SEARCH - O(log n)
# =============================================================================
def binary_search(arr, target):
    """
    Search for target in SORTED array using divide-and-conquer
    Time Complexity: O(log n) - eliminate half each time
    Space Complexity: O(1) - no extra space needed
    
    IMPORTANT: Array must be sorted!
    Example: binary_search([1, 2, 3, 4, 5], 4) -> 3
    """
    left, right = 0, len(arr) - 1

    while left <= right:
        mid = (left + right) // 2  # Find middle index

        if arr[mid] == target:
            return mid  # Found it!
        elif arr[mid] < target:
            left = mid + 1  # Search right half
        else:
            right = mid - 1  # Search left half

    return -1  # Not found

# Recursive version (alternative implementation)


def binary_search_recursive(arr, target, left=0, right=None):
    """
    Recursive implementation of binary search
    """
    if right is None:
        right = len(arr) - 1

    if left > right:
        return -1

    mid = (left + right) // 2

    if arr[mid] == target:
        return mid
    elif arr[mid] < target:
        return binary_search_recursive(arr, target, mid + 1, right)
    else:
        return binary_search_recursive(arr, target, left, mid - 1)


# Test Binary Search
print("\n=== BINARY SEARCH ===")
sorted_arr = [1, 2, 3, 4, 5, 7, 8, 9]
print(f"Sorted Array: {sorted_arr}")
print(f"Search for 4: index {binary_search(sorted_arr, 4)}")  # Should return 3
# Should return -1
print(f"Search for 6: index {binary_search(sorted_arr, 6)}")
# Should return 5
print(
    f"Recursive search for 7: index {binary_search_recursive(sorted_arr, 7)}")
