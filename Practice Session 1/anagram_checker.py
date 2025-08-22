def is_anagram(s, t):
    return sorted(s) == sorted(t)


print(is_anagram("listen", "silent"))  # True
print(is_anagram("rat", "car"))        # False

from collections import Counter

def are_anagrams(word1, word2):
    return Counter(word1) == Counter(word2)

# Test cases
print(are_anagrams("listen", "silent"))  # True
print(are_anagrams("triangle", "integral"))  # True
print(are_anagrams("apple", "pale"))  # False
