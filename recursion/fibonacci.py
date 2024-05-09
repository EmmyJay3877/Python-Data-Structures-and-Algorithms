"""
The Fibonacci numbers, commonly denoted F(n) form a sequence, called 
the Fibonacci sequence, such that each number is the sum of the 
two preceding ones, starting from 0 and 1. That is,

F(0) = 0, F(1) = 1
F(n) = F(n - 1) + F(n - 2), for n > 1.
Given n, calculate F(n).
"""

# The recursive method
def _fib(n):
    if n == 0 or n == 1:
        return n
    return _fib(n-1) + _fib(n-2)

# The Dynamic method
def fib(n):
    memo = {}
    if n == 0 or n == 1:
        return n
    if n not in memo:
        memo[n] = fib(n-1) + fib(n-2)
    return memo[n]