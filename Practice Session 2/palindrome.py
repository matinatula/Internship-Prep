# =============================================================================
# PROBLEM 4: PALINDROME CHECK (Easy-Medium)
# =============================================================================
def is_palindrome(s):
    """
    Check if a string is a palindrome (reads same forwards and backwards)
    Ignore spaces and case
    Example: "A man a plan a canal Panama" -> True
    """
    # Remove non-alphanumeric and convert to lowercase
    cleaned = ''.join(char.lower() for char in s if char.isalnum())
    return cleaned == cleaned[::-1]


# Test cases
print("\nProblem 4 - Palindrome:")
print(is_palindrome("racecar"))                           # Should output: True
print(is_palindrome("A man a plan a canal Panama"))       # Should output: True
# Should output: False
print(is_palindrome("hello"))
