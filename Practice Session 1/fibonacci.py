# Recursive
def fib_recursive(n):
    if n <= 1:
        return n
    return fib_recursive(n-1) + fib_recursive(n-2)

# Iterative


def fib_iterative(n):
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a+b
    return a


print(fib_recursive(6))  # 8
print(fib_iterative(6))  # 8
