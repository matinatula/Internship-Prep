# Problem A: Remove duplicates from array and return sorted result
def remove_duplicates_and_sort(arr):
    """
    Remove duplicates and return sorted array
    Example: [3, 1, 2, 1, 3, 4] -> [1, 2, 3, 4]
    """
    # Method 1: Using set (most efficient)
    return sorted(list(set(arr)))

    # Method 2: Manual way (if interviewer wants to see logic)
    # unique = []
    # for item in arr:
    #     if item not in unique:
    #         unique.append(item)
    # return sorted(unique)

# Problem B: Check if two strings are anagrams


def are_anagrams(str1, str2):
    """
    Check if two strings are anagrams
    Example: "listen" and "silent" -> True
    """
    # Method 1: Sort both strings
    return sorted(str1.lower()) == sorted(str2.lower())

    # Method 2: Count frequency (alternative approach)
    # if len(str1) != len(str2):
    #     return False
    #
    # count = {}
    # for char in str1.lower():
    #     count[char] = count.get(char, 0) + 1
    #
    # for char in str2.lower():
    #     if char not in count:
    #         return False
    #     count[char] -= 1
    #     if count[char] == 0:
    #         del count[char]
    #
    # return len(count) == 0


# Test the solutions
print("Problem A - Remove Duplicates and Sort:")
print(remove_duplicates_and_sort([3, 1, 2, 1, 3, 4]))    # [1, 2, 3, 4]
print(remove_duplicates_and_sort([5, 5, 5, 1]))          # [1, 5]

print("\nProblem B - Anagrams:")
print(are_anagrams("listen", "silent"))    # True
print(are_anagrams("hello", "world"))      # False
print(are_anagrams("A", "a"))              # True
