def group_anagrams(words):
    groups = {}
    for word in words:
        key = tuple(sorted(word))   # sorted tuple works as hashable key
        groups.setdefault(key, []).append(word)
    return list(groups.values())



words = ["listen", "silent", "enlist", "hello", "olleh", "world"]
print(group_anagrams(words))
# [['listen', 'silent', 'enlist'], ['hello', 'olleh'], ['world']]
