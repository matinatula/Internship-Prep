# =============================================================================
# PROBLEM 2: STRING MANIPULATION (Easy)
# =============================================================================
def count_vowels(s):
    """
    Count the number of vowels in a string
    Example: "hello world" -> 3 (e, o, o)
    """
    vowels = "aeiouAEIOU"
    count = 0
    for char in s:
        if char in vowels:
            count += 1
    return count


# Test cases
print("\nProblem 2 - Count Vowels:")
print(count_vowels("hello world"))    # Should output: 3
print(count_vowels("python"))         # Should output: 1
print(count_vowels("xyz"))            # Should output: 0
