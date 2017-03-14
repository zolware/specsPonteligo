# -*- coding: utf-8 -*-

"""
**Module Docstring:**
Some info

"""

# import numpy as np


def fib(n):
    """print the Fibonacci series up to n.
    :param n: an input argument
    """
    a, b = 0, 1
    while b < n:
        print(b, end=' ')
        a, b = b, a+b
    print()


def fib2(n):
    """return the Fibonacci series up to n.
    :param n: an input argument
    :returns: the Fibonacci series up to n
    """
    result = []
    a, b = 0, 1
    while b < n:
        result.append(b)
        a, b = b, a+b
    return result
