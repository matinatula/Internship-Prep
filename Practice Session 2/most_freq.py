# =============================================================================
# PROBLEM 5: FREQUENCY COUNTING (Medium)
# =============================================================================
def find_most_frequent(arr):
    """
    Find the most frequently occurring element in an array
    Example: [1, 2, 2, 3, 3, 3] -> 3
    """
    if not arr:
        return None

    frequency = {}
    for num in arr:
        frequency[num] = frequency.get(num, 0) + 1

    max_count = max(frequency.values())
    for num, count in frequency.items():
        if count == max_count:
            return num


# Test cases
print("\nProblem 5 - Most Frequent:")
print(find_most_frequent([1, 2, 2, 3, 3, 3]))    # Should output: 3
print(find_most_frequent([1, 1, 2, 2]))          # Should output: 1 or 2
print(find_most_frequent([5]))                    # Should output: 5
