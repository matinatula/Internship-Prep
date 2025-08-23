def group_anagrams(words):
    anagrams = {}
    for word in words:
        key = "".join(sorted(word))   # canonical form
        if key not in anagrams:
            anagrams[key] = []
        anagrams[key].append(word)
    return list(anagrams.values())


# Example
print(group_anagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))
# [['eat', 'tea', 'ate'], ['tan', 'nat'], ['bat']]
