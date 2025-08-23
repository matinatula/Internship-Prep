Perfect 👌 I’ll make you a **cheat sheet** of all *possible/likely* questions based on what you + your friend said, plus the standard easy DSA/OOP ones they ask in such exams.

---

# 🚀 Cheat Sheet for Your Test (MCQ + Code)

---

## 🔹 OOP (MCQ Style)

* What is **OOP**? (Encapsulation, Inheritance, Polymorphism, Abstraction)
* Difference between **class vs object**.
* Constructor in Python → `__init__`.
* **Access modifiers** → public, protected `_var`, private `__var`.
* `self` = reference to current object.
* Static method → `@staticmethod`, Class method → `@classmethod`.
* Inheritance syntax:

  ```python
  class Child(Parent):
      pass
  ```
* Polymorphism = same function name works differently depending on object.

---

## 🔹 String & Array / Dict (Code)

### 1. Reverse a string

```python
s[::-1]
```

### 2. Palindrome check

```python
def is_palindrome(s):
    return s == s[::-1]
```

### 3. Frequency of chars

```python
from collections import Counter
Counter("banana")  # {'b':1,'a':3,'n':2}
```

### 4. First non-repeating char

```python
def first_unique(s):
    freq = {}
    for c in s:
        freq[c] = freq.get(c,0)+1
    for c in s:
        if freq[c] == 1:
            return c
    return None
```

### 5. Check anagram (2 words)

```python
sorted(a) == sorted(b)
```

### 6. Group anagrams (list → dict)

```python
def group_anagrams(words):
    anagrams = {}
    for word in words:
        key = "".join(sorted(word))
        anagrams.setdefault(key, []).append(word)
    return list(anagrams.values())
```

### 7. Remove duplicates from list

```python
list(set([1,2,2,3]))
```

### 8. Two-sum problem

```python
def two_sum(nums, target):
    seen = {}
    for i, num in enumerate(nums):
        if target - num in seen:
            return [seen[target-num], i]
        seen[num] = i
```

---

## 🔹 Stack / Parentheses

### 9. Valid parentheses

```python
def valid(s):
    stack = []
    pairs = {')':'(', ']':'[', '}':'{'}
    for ch in s:
        if ch in '([{':
            stack.append(ch)
        elif not stack or stack[-1]!=pairs[ch]:
            return False
        else:
            stack.pop()
    return not stack
```

### 10. Parentheses scoring

```python
def paren_score(s):
    stack=[0]
    for ch in s:
        if ch=='(':
            stack.append(0)
        else:
            v=stack.pop()
            stack[-1]+=max(2*v,1)
    return stack.pop()
```

---

## 🔹 Conversions

### 11. Integer to Roman

```python
def int_to_roman(num):
    val=[1000,900,500,400,100,90,50,40,10,9,5,4,1]
    syb=["M","CM","D","CD","C","XC","L","XL","X","IX","V","IV","I"]
    res=""
    for i,v in enumerate(val):
        while num>=v:
            res+=syb[i]; num-=v
    return res
```

### 12. Roman to Integer

```python
def roman_to_int(s):
    vals={'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
    total=0
    for i in range(len(s)):
        if i+1<len(s) and vals[s[i]]<vals[s[i+1]]:
            total-=vals[s[i]]
        else:
            total+=vals[s[i]]
    return total
```

---

## 🔹 Misc (Likely Quickies)

### 13. Factorial (recursive)

```python
def fact(n): return 1 if n<=1 else n*fact(n-1)
```

### 14. Fibonacci (iterative)

```python
def fib(n):
    a,b=0,1
    for _ in range(n): a,b=b,a+b
    return a
```

### 15. Find second largest

```python
def second_largest(arr):
    first=second=float('-inf')
    for n in arr:
        if n>first:
            second,first=first,n
        elif first>n>second:
            second=n
    return second
```

### 16. Remove vowels from string

```python
"".join(c for c in s if c not in "aeiouAEIOU")
```

### 17. Reverse words in sentence

```python
" ".join(s.split()[::-1])
```

---

🔥 If I were you, I’d prepare mostly:

* **String tricks** (palindrome, reverse, frequency, anagram, unique chars)
* **Dict tricks** (frequency, two-sum, anagram grouping)
* **Stack tricks** (valid parentheses, scoring)
* **Conversions** (int ↔ roman)
* **Simple OOP MCQs**

---

👉 Do you want me to make a **final “super-condensed 1-page notes”** version (just formulas + code skeletons, no explanation) so you can literally revise in **5 min before exam**?
