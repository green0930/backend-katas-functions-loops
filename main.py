#!/usr/bin/env python
"""Implements math functions without using operators,
except for '+' and '-'.
"""

__author__ = "???"


def add(x, y):
    """Add two integers."""
    return x + y
    print(add(2, 4))


def multiply(x, y):
    """Multiply x with y using the add() function above."""
    total = 0
    for i in range(abs(y)):
        total = add(x, total)
    if y < 0:
        return -total
    return total
    print(multiply(6, -8))


def power(x, n):
    """Raise x to power n, where n >= 0, using the functions above."""
    total = 1
    for i in range(n):
        total = multiply(x, total)
    return total
    print(power(2, 8))


def factorial(x):
    """Compute the factorial of x, where x > 0, using the functions above."""
    fact = 1
    for i in range(2, x+1):
        fact = power(x, fact)
        return fact
    print(factorial(4))


def fibonacci(n):
    """Compute the nth term of fibonacci sequence using the functions above."""
    # your code here
    return


if __name__ == '__main__':
    # your code to call functions above
    pass
