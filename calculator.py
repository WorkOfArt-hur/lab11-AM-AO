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

def divide(a,b):
    result = 0
    try:
        result = a/b
        return result
    except:
        raise ZeroDivisionError
        
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
    


