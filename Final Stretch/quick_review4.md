Perfect 🔥 this will be your **1-page cram sheet** for tomorrow — OOP + DSA + Code skeletons + MCQ key points.

---

# 🚀 Final Revision Cheat Sheet (OOP + DSA)

---

## 🔹 OOP Quick Facts (MCQs)

* **Encapsulation** → Wrapping data & methods into a class.
* **Inheritance** → Reuse code from parent.
* **Polymorphism** → Same name, many forms.
* **Abstraction** → Hide details, show functionality.
* **Class vs Object** → Blueprint vs instance.
* **Constructor** → `__init__(self, ...)`
* **Access Modifiers** → public: `var`, protected: `_var`, private: `__var`
* **self** → current instance reference.
* **Static method** → `@staticmethod` (no self/cls).
* **Class method** → `@classmethod` (first arg is cls).
* **Overriding** → Child redefines parent method.
* **Overloading** → Not directly supported (last def wins).
* **Multiple inheritance** → Allowed.
* **Operator overloading** → Supported (e.g. `__add__`).

✅ MCQ Keywords: constructor → `__init__`, self → instance, multiple inheritance → allowed, polymorphism = many forms.

---

## 🔹 String / Dict / Array Code Patterns

```python
# Reverse
s[::-1]

# Palindrome
s == s[::-1]

# Frequency
from collections import Counter
Counter("banana")  # {'b':1,'a':3,'n':2}

# First unique char
def first_unique(s):
    freq={}
    for c in s: freq[c]=freq.get(c,0)+1
    for c in s:
        if freq[c]==1: return c
    return None

# Anagram (2 words)
sorted(a) == sorted(b)

# Group Anagrams (list)
def group_anagrams(words):
    d={}
    for w in words:
        key="".join(sorted(w))
        d.setdefault(key,[]).append(w)
    return list(d.values())

# Remove duplicates
list(set(arr))

# Two-Sum (O(n))
def two_sum(nums,target):
    seen={}
    for i,n in enumerate(nums):
        if target-n in seen: return [seen[target-n],i]
        seen[n]=i
```

---

## 🔹 Stack / Parentheses

```python
# Valid parentheses
def valid(s):
    stack=[]; pairs={')':'(',']':'[','}':'{'}
    for ch in s:
        if ch in '([{': stack.append(ch)
        elif not stack or stack[-1]!=pairs[ch]: return False
        else: stack.pop()
    return not stack

# Parentheses scoring
def paren_score(s):
    stack=[0]
    for ch in s:
        if ch=='(': stack.append(0)
        else:
            v=stack.pop()
            stack[-1]+=max(2*v,1)
    return stack.pop()
```

---

## 🔹 Conversions

```python
# Int → Roman
def int_to_roman(num):
    val=[1000,900,500,400,100,90,50,40,10,9,5,4,1]
    syb=["M","CM","D","CD","C","XC","L","XL","X","IX","V","IV","I"]
    res=""
    for i,v in enumerate(val):
        while num>=v:
            res+=syb[i]; num-=v
    return res

# Roman → Int
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

## 🔹 Misc Quickies

```python
# Factorial
def fact(n): return 1 if n<=1 else n*fact(n-1)

# Fibonacci
def fib(n):
    a,b=0,1
    for _ in range(n): a,b=b,a+b
    return a

# Second largest
def second_largest(arr):
    first=second=float('-inf')
    for n in arr:
        if n>first: second,first=first,n
        elif first>n>second: second=n
    return second

# Reverse words
" ".join(s.split()[::-1])
```

---

## 🔹 Complexity Cheats

* **Reverse / Palindrome** → O(n)
* **Anagram (sort)** → O(n log n)
* **Anagram (dict count)** → O(n) ✅ faster
* **Two-sum with dict** → O(n)
* **Two-sum with loops** → O(n²)
* **Valid parentheses (stack)** → O(n), space O(n)
* **Palindrome two-pointer** → O(1) space

---

✅ This single sheet is enough:

* **Top OOP MCQs**
* **Most common string/dict/stack problems**
* **Conversions**
* **Complexity**

---

Do you want me to also make a **tiny version (like 20–30 lines only)** that you can screenshot and revise literally in **2 minutes before exam**?
