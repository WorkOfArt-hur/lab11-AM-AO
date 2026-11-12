"""
calculator.py
- Defines functions used to create a simple calculator

One function per operation, in order.
"""
import math
def add(a,b):
    return a + b
def sub(a, b):
    return a - b
def mul(a,b):
    return a * b
def div(a, b):
    c = b/a
    if a == 0:
        raise ZeroDivisionError
    else:
        return c
def log(a, b):
    try:
        c = math.log(b,a)
    except ValueError:
        raise
    else:
        return c
def exp(a, b):
    return a ** b

