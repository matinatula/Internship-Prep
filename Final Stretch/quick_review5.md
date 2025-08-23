Perfect 😎 here’s the **ultra-condensed 2-min revision sheet** — all essentials in **\~30 lines**, ready to screenshot:

---

# ⚡ 2-Minute Python OOP + DSA Cheat Sheet

---

## **OOP Quick MCQ**

* Encapsulation = wrap data + methods
* Inheritance = reuse parent code
* Polymorphism = same name, many forms
* Abstraction = hide details, show functionality
* Constructor = `__init__(self,...)`
* self = current instance
* Access: public `var`, protected `_var`, private `__var`
* Static method = `@staticmethod`, Class method = `@classmethod`
* Method overriding = child redefines parent
* Multiple inheritance = allowed

---

## **Strings / List / Dict**

```python
s[::-1]           # reverse
s==s[::-1]        # palindrome
Counter(s)        # frequency
sorted(a)==sorted(b) # anagram 2 words
list(set(arr))    # remove duplicates
" ".join(s.split()[::-1]) # reverse words
```

**Group Anagrams**

```python
d={}
for w in words: d.setdefault("".join(sorted(w)),[]).append(w)
```

**Two-Sum**

```python
seen={}
for i,n in enumerate(nums):
    if target-n in seen: return [seen[target-n],i]
    seen[n]=i
```

---

## **Stack / Parentheses**

```python
stack=[]
for ch in s:
    if ch=='(': stack.append(0)
    else: v=stack.pop(); stack[-1]+=max(2*v,1)
```

* `"()"=1`, `"(())"=2`, `"(()())"=4`

```python
# valid parentheses
pairs={')':'(',']':'[','}':'{'}
stack=[]
for ch in s:
    if ch in '([{': stack.append(ch)
    elif not stack or stack[-1]!=pairs[ch]: False
    else: stack.pop()
```

---

## **Conversions**

```python
# int->roman
val=[1000,900,500,400,100,90,50,40,10,9,5,4,1]
syb=["M","CM","D","CD","C","XC","L","XL","X","IX","V","IV","I"]
res=""; i=0
while num>0:
    for _ in range(num//val[i]): res+=syb[i]; num-=val[i]
    i+=1

# roman->int
vals={'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
total=0
for i in range(len(s)):
    if i+1<len(s) and vals[s[i]]<vals[s[i+1]]: total-=vals[s[i]]
    else: total+=vals[s[i]]
```

---

## **Quick Misc**

```python
def fact(n): return 1 if n<=1 else n*fact(n-1)
def fib(n):
    a,b=0,1
    for _ in range(n): a,b=b,a+b
    return a
def second_largest(arr):
    f,s=float('-inf'),float('-inf')
    for n in arr:
        if n>f: s,f=f,n
        elif f>n>s: s=n
    return s
```

---

## **Complexity Short**

* Reverse / Palindrome = O(n)
* Anagram (sort) = O(n log n), (dict) = O(n) ✅
* Two-sum dict = O(n)
* Two-sum loops = O(n²)
* Parentheses stack = O(n)

---

This is literally everything **you need to glance once** and walk into the exam confident 😎.

---

If you want, I can also make a **tiny “cheat sheet image” version** for your phone so you can revise even **while in transport or bathroom 😏**. Do you want me to do that?
