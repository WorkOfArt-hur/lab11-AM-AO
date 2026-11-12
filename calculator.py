"""
calculator.py
- Defines functions used to create a simple calculator

One function per operation, in order.
"""
import math

# First example
def square_root(a):
    try:
        assert a >= 0
        return math.sqrt(a)
    except:
        raise ValueError
    
def hypotenuse(a, b):
    return math.hypot(a, b)
    
def add(a, b): 
    return a + b

def subtract(a,b):
    return a - b

def multiply(a, b):
    return a*b

def divide(a,b):
    try:
        return a/b
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
    


