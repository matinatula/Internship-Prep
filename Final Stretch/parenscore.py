def paren_score(s):
    stack = []
    score = 0
    for ch in s:
        if ch == "(":
            stack.append(ch)
        else:  # closing
            stack.pop()
            score += 1
    return score


print(paren_score("()"))    # 1
print(paren_score("(())"))  # 2
