Perfect 👍 Let’s cover the **coding part** now (2 questions).
They said the focus will be **list comprehension, matrix, array searching/sorting, tree traversal** → so I’ll give you **all possible coding questions + their solutions in Python**.

---

# 🔹 1. **List Comprehension Coding Questions**

✅ Possible exam-style questions:

**Q1. Generate squares of numbers from 1 to n using list comprehension.**

```python
n = 5
squares = [x**2 for x in range(1, n+1)]
print(squares)   # [1, 4, 9, 16, 25]
```

**Q2. Extract all even numbers from a list.**

```python
nums = [1,2,3,4,5,6]
evens = [x for x in nums if x % 2 == 0]
print(evens)  # [2,4,6]
```

**Q3. Flatten a 2D matrix into a 1D list.**

```python
matrix = [[1,2],[3,4],[5,6]]
flattened = [x for row in matrix for x in row]
print(flattened)  # [1,2,3,4,5,6]
```

---

# 🔹 2. **Matrix Manipulation Coding Questions**

✅ High chance of one question here.

**Q1. Transpose a matrix.**

```python
matrix = [[1,2,3],[4,5,6],[7,8,9]]
transpose = [[matrix[j][i] for j in range(len(matrix))] for i in range(len(matrix[0]))]
print(transpose)   # [[1,4,7],[2,5,8],[3,6,9]]
```

**Q2. Rotate a matrix 90° clockwise.**

```python
def rotate(matrix):
    return [list(row)[::-1] for row in zip(*matrix)]

matrix = [[1,2,3],[4,5,6],[7,8,9]]
print(rotate(matrix))  # [[7,4,1],[8,5,2],[9,6,3]]
```

**Q3. Print a matrix in spiral order.**

```python
def spiral(matrix):
    res = []
    while matrix:
        res += matrix.pop(0)
        if matrix and matrix[0]:
            for row in matrix: res.append(row.pop())
        if matrix: res += matrix.pop()[::-1]
        if matrix and matrix[0]:
            for row in matrix[::-1]: res.append(row.pop(0))
    return res

print(spiral([[1,2,3],[4,5,6],[7,8,9]])) # [1,2,3,6,9,8,7,4,5]
```

---

# 🔹 3. **Array Searching Coding Questions**

✅ Classic exam pick.

**Q1. Linear search.**

```python
def linear_search(arr, target):
    for i, val in enumerate(arr):
        if val == target:
            return i
    return -1

print(linear_search([10,20,30,40], 30))  # 2
```

**Q2. Binary search.**

```python
def binary_search(arr, target):
    l, r = 0, len(arr)-1
    while l <= r:
        mid = (l+r)//2
        if arr[mid] == target: return mid
        elif arr[mid] < target: l = mid+1
        else: r = mid-1
    return -1

print(binary_search([1,2,3,4,5], 4))  # 3
```

---

# 🔹 4. **Array Sorting Coding Questions**

✅ They may ask you to implement a basic one.

**Q1. Bubble sort.**

```python
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

print(bubble_sort([5,1,4,2,8]))  # [1,2,4,5,8]
```

**Q2. Insertion sort.**

```python
def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i-1
        while j >= 0 and key < arr[j]:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = key
    return arr

print(insertion_sort([5,2,9,1,5,6]))  # [1,2,5,5,6,9]
```

**Q3. Just use Python’s built-in (for large inputs).**

```python
arr = [5,2,9,1,5,6]
print(sorted(arr))  # [1,2,5,5,6,9]
```

---

# 🔹 5. **Tree Traversal Coding Questions**

✅ Common interview-style problem.

**Q1. Inorder traversal (DFS).**

```python
class Node:
    def __init__(self, val):
        self.val = val
        self.left = self.right = None

def inorder(root):
    if root:
        inorder(root.left)
        print(root.val, end=" ")
        inorder(root.right)

root = Node(1)
root.left, root.right = Node(2), Node(3)
inorder(root)  # 2 1 3
```

**Q2. Preorder traversal.**

```python
def preorder(root):
    if root:
        print(root.val, end=" ")
        preorder(root.left)
        preorder(root.right)
```

**Q3. BFS (Level order traversal).**

```python
from collections import deque
def bfs(root):
    q = deque([root])
    while q:
        node = q.popleft()
        print(node.val, end=" ")
        if node.left: q.append(node.left)
        if node.right: q.append(node.right)
```

---

# 🎯 Final Exam Probability

If they give **2 coding questions**, they’ll very likely be:

1. **Matrix manipulation** (transpose, rotate, or spiral)
2. **Searching/sorting OR tree traversal**

---

👉 Do you want me to **pick the 2 most probable exact coding questions** (with final code ready) like I did for the MCQs, so you can memorize just those?
