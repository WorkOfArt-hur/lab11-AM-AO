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
   c = b/a
   if a == 0:
       raise ZeroDivisionError
   else:
       return c
        
def logarithm(a,b):
    try:
        c = math.log(b,a)
    except ValueError:
        raise
    else:
        return c
    
def exponent(a,b):
    return a**b
    


