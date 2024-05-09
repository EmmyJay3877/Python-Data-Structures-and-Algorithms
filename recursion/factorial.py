"""
Implement the factorial function using recursion.

Factorial Function (factorial):

Calculates the factorial of a non-negative integer n using recursion.

The factorial of n is the product of all positive integers less than or equal to n.
"""

def factorial(n):
    # Implmenet this function
    if n == 0:
        return 1 
    else:
        return n * factorial(n-1)