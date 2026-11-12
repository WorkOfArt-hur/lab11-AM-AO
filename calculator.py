"""
calculator.py
- Defines functions used to create a simple calculator

One function per operation, in order.
"""
import math

# First example
def add(a, b): 
    return a + b

def subtract(a,b):
    return a - b

def multiply(a, b):
    return a*b

def div(a,b):
    c = b/a
    if a == 0:
        raise ZeroDivisionError
    else:
        return c
        
def logarithm(a,b):
    result = 0
    try:
        assert a > 1
        assert b > 0
        result = math.log(a,b)
        return result
    except:
        raise ValueError
    
def exponent(a,b):
    return a**b
    


