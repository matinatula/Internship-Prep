# =============================================================================
# 4. MERGE SORT - O(n log n)
# =============================================================================
def merge_sort(arr):
    """
    Efficient divide-and-conquer sorting algorithm
    Time Complexity: O(n log n) - always, even worst case
    Space Complexity: O(n) - needs extra space for merging
    
    Example: merge_sort([38, 27, 43, 3]) -> [3, 27, 38, 43]
    """
    if len(arr) <= 1:
        return arr  # Base case: single element or empty

    # Divide: Split array in half
    mid = len(arr) // 2
    left_half = arr[:mid]
    right_half = arr[mid:]

    # Conquer: Recursively sort both halves
    left_sorted = merge_sort(left_half)
    right_sorted = merge_sort(right_half)

    # Combine: Merge the sorted halves
    return merge(left_sorted, right_sorted)


def merge(left, right):
    """
    Helper function to merge two sorted arrays
    """
    result = []
    i = j = 0

    # Compare elements from both arrays and add smaller one
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    # Add remaining elements (if any)
    result.extend(left[i:])
    result.extend(right[j:])

    return result


# Test Merge Sort
print("\n=== MERGE SORT ===")
unsorted_arr2 = [38, 27, 43, 3, 9, 82, 10]
print(f"Original: {unsorted_arr2}")
merge_sorted = merge_sort(unsorted_arr2)
print(f"Merge Sorted: {merge_sorted}")

# =============================================================================
# BONUS: SELECTION SORT - O(n²) (Simple alternative to bubble sort)
# =============================================================================


def selection_sort(arr):
    """
    Find minimum element and place it at the beginning
    Time Complexity: O(n²) - nested loops
    Space Complexity: O(1) - sorts in place
    """
    n = len(arr)

    for i in range(n):
        # Find minimum element in remaining array
        min_idx = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j

        # Swap the found minimum element with the first element
        arr[i], arr[min_idx] = arr[min_idx], arr[i]

    return arr


# Test Selection Sort
print("\n=== SELECTION SORT (BONUS) ===")
unsorted_arr3 = [29, 10, 14, 37, 13]
print(f"Original: {unsorted_arr3}")
selection_sorted = selection_sort(unsorted_arr3.copy())
print(f"Selection Sorted: {selection_sorted}")

# =============================================================================
# ALGORITHM COMPARISON SUMMARY
# =============================================================================
print("\n" + "="*60)
print("ALGORITHM COMPLEXITY SUMMARY")
print("="*60)
print("SEARCHING:")
print("  Linear Search:   O(n)       - Works on any array")
print("  Binary Search:   O(log n)   - Requires sorted array")
print()
print("SORTING:")
print("  Bubble Sort:     O(n²)      - Simple but slow")
print("  Selection Sort:  O(n²)      - Simple but slow")
print("  Merge Sort:      O(n log n) - Fast and stable")
print("  Built-in sorted(): O(n log n) - Use this in real code!")

# =============================================================================
# EXAM-STYLE QUESTIONS YOU MIGHT GET
# =============================================================================
print("\n" + "="*60)
print("LIKELY EXAM QUESTIONS")
print("="*60)


def exam_question_1(arr, target):
    """
    EXAM QUESTION 1: Find if a target exists in a sorted array
    Input: sorted_array = [1, 3, 5, 7, 9, 11], target = 7
    Output: True (or return the index: 3)
    
    Expected: Binary search implementation
    """
    # Solution using Binary Search - O(log n)
    left, right = 0, len(arr) - 1

    while left <= right:
        mid = (left + right) // 2

        if arr[mid] == target:
            return True  # Found it! (or return mid for index)
        elif arr[mid] < target:
            left = mid + 1  # Search right half
        else:
            right = mid - 1  # Search left half

    return False  # Not found


def exam_question_2(arr):
    """
    EXAM QUESTION 2: Sort an array of integers in ascending order
    Input: [64, 34, 25, 12, 22, 11, 90]
    Output: [11, 12, 22, 25, 34, 64, 90]
    
    Expected: Any sorting algorithm (or built-in sorted())
    """
    # Solution 1: Use built-in (most efficient for real code)
    return sorted(arr)

    # Solution 2: Bubble Sort implementation (if they want to see algorithm)
    # n = len(arr)
    # for i in range(n):
    #     for j in range(0, n - i - 1):
    #         if arr[j] > arr[j + 1]:
    #             arr[j], arr[j + 1] = arr[j + 1], arr[j]
    # return arr


# Test the exam questions
print("TESTING EXAM QUESTIONS:")
print("\n--- Question 1: Find in sorted array ---")
sorted_test = [1, 3, 5, 7, 9, 11, 13]
print(f"Array: {sorted_test}")
print(f"Find 7: {exam_question_1(sorted_test, 7)}")    # Should return True
print(f"Find 4: {exam_question_1(sorted_test, 4)}")    # Should return False

print("\n--- Question 2: Sort array ---")
unsorted_test = [64, 34, 25, 12, 22, 11, 90]
print(f"Original: {unsorted_test}")
# Should return sorted array
print(f"Sorted: {exam_question_2(unsorted_test)}")

print("\n" + "="*60)
print("ADDITIONAL EXAM-STYLE QUESTIONS")
print("="*60)


def exam_question_3(arr):
    """
    EXAM QUESTION 3: Find the maximum element in an array
    Input: [3, 7, 1, 9, 4, 6]
    Output: 9
    
    This tests basic array traversal and comparison logic
    """
    if not arr:  # Handle empty array
        return None

    max_val = arr[0]  # Assume first element is max
    for i in range(1, len(arr)):
        if arr[i] > max_val:
            max_val = arr[i]
    return max_val

    # Alternative one-liner: return max(arr)


def exam_question_4(arr, target):
    """
    EXAM QUESTION 4: Find the first occurrence of target in unsorted array
    Input: [4, 2, 7, 2, 9, 2], target = 2
    Output: 1 (index of first occurrence)
    
    This tests linear search implementation
    """
    for i in range(len(arr)):
        if arr[i] == target:
            return i  # Return index of first occurrence
    return -1  # Not found


def exam_question_5(arr):
    """
    EXAM QUESTION 5: Reverse an array in-place
    Input: [1, 2, 3, 4, 5]
    Output: [5, 4, 3, 2, 1]
    
    This tests array manipulation and two-pointer technique
    """
    left, right = 0, len(arr) - 1

    while left < right:
        # Swap elements at left and right positions
        arr[left], arr[right] = arr[right], arr[left]
        left += 1
        right -= 1

    return arr

    # Alternative: return arr[::-1]  # Creates new array


# Test additional exam questions
print("\n--- Question 3: Find maximum ---")
test_arr3 = [3, 7, 1, 9, 4, 6]
print(f"Array: {test_arr3}")
print(f"Maximum: {exam_question_3(test_arr3)}")       # Should return 9

print("\n--- Question 4: Find first occurrence ---")
test_arr4 = [4, 2, 7, 2, 9, 2]
print(f"Array: {test_arr4}")
# Should return 1
print(f"First occurrence of 2: {exam_question_4(test_arr4, 2)}")

print("\n--- Question 5: Reverse array ---")
test_arr5 = [1, 2, 3, 4, 5]
print(f"Original: {test_arr5}")
# Use copy to preserve original
reversed_arr = exam_question_5(test_arr5.copy())
# Should return [5, 4, 3, 2, 1]
print(f"Reversed: {reversed_arr}")

# =============================================================================
# QUICK IMPLEMENTATION TIPS FOR EXAM
# =============================================================================
print("\n📝 EXAM IMPLEMENTATION TIPS:")
print("1. Binary Search: Remember left <= right condition")
print("2. Sorting: Use built-in sorted() if allowed, otherwise bubble sort is easiest")
print("3. Always check edge cases: empty array, single element")
print("4. Binary search ONLY works on sorted arrays!")
print("5. For interviews, mention time complexity if asked")

print("\n🎯 MOST LIKELY TO BE ASKED:")
print("   1. Binary Search (very common)")
print("   2. Simple sorting algorithm")
print("   3. Linear search variations")

print("\n✨ You're ready! Practice these patterns and you'll ace the algorithms section!")
