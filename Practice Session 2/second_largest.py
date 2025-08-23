# =============================================================================
# PROBLEM 1: ARRAY MANIPULATION (Easy-Medium)
# =============================================================================
def find_second_largest(arr):
    """
    Find the second largest number in an array
    Example: [1, 3, 4, 5, 2] -> 4
    """
    if len(arr) < 2:
        return None

    first = second = float('-inf')
    for num in arr:
        if num > first:
            second = first
            first = num
        elif num > second and num != first:
            second = num

    return second if second != float('-inf') else None


# Test cases
print("Problem 1 - Second Largest:")
print(find_second_largest([1, 3, 4, 5, 2]))  # Should output: 4
print(find_second_largest([5, 5, 5]))        # Should output: None
print(find_second_largest([1, 2]))           # Should output: 1
