def fibonacci(n):
    """
    Return the nth Fibonacci number
    Fibonacci sequence: 0, 1, 1, 2, 3, 5, 8, 13, ...
    """
    if n <= 1:
        return n
    return fibonacci(n-1) + fibonacci(n-2)

# More efficient version using dynamic programming


def fibonacci_dp(n):
    if n <= 1:
        return n

    a, b = 0, 1
    for i in range(2, n + 1):
        a, b = b, a + b
    return b


# Test cases
print("\nBonus - Fibonacci:")
print(fibonacci_dp(0))    # Should output: 0
print(fibonacci_dp(1))    # Should output: 1
print(fibonacci_dp(5))    # Should output: 5
print(fibonacci_dp(10))   # Should output: 55
