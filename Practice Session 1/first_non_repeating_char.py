def first_unique_char(s):
    count = {}
    for ch in s:
        count[ch] = count.get(ch, 0) + 1
    for i, ch in enumerate(s):
        if count[ch] == 1:
            return i
    return -1


# Test
print(first_unique_char("leetcode"))  # 0
print(first_unique_char("aabb"))      # -1
