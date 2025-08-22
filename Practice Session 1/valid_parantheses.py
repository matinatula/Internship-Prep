def is_valid_parentheses(s):
    stack = []
    mapping = {')': '(', ']': '[', '}': '{'}
    for char in s:
        if char in mapping:
            if not stack or stack.pop() != mapping[char]:
                return False
        else:
            stack.append(char)
    return not stack


# Test
print(is_valid_parentheses("()[]{}"))  # True
print(is_valid_parentheses("(]"))      # False
