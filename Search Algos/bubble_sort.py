# =============================================================================
# 3. BUBBLE SORT - O(n²)
# =============================================================================
def bubble_sort(arr):
    """
    Simple sorting algorithm - repeatedly swaps adjacent elements
    Time Complexity: O(n²) - nested loops
    Space Complexity: O(1) - sorts in place
    
    Example: bubble_sort([64, 34, 25, 12]) -> [12, 25, 34, 64]
    """
    n = len(arr)

    # Traverse through all array elements
    for i in range(n):
        swapped = False  # Optimization: track if any swaps made

        # Last i elements are already sorted
        for j in range(0, n - i - 1):
            # Swap if the element found is greater than the next element
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True

        # If no swapping happened, array is sorted
        if not swapped:
            break

    return arr


# Test Bubble Sort
print("\n=== BUBBLE SORT ===")
unsorted_arr = [64, 34, 25, 12, 22, 11, 90]
print(f"Original: {unsorted_arr}")
bubble_sorted = bubble_sort(unsorted_arr.copy())  # Use copy to keep original
print(f"Bubble Sorted: {bubble_sorted}")
