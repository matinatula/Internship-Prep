def paren_score(s):
    stack = [0]
    for ch in s:
        if ch == "(":
            stack.append(0)
        else:
            v = stack.pop()
            stack[-1] += max(2*v, 1)
    return stack.pop()


print(paren_score("()"))     # 1
print(paren_score("(())"))   # 2
print(paren_score("(()())"))  # 4
