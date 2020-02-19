"""
Examples of functions that take inputs and return outputs

CMS 195, Spring 2020
"""

from math import pi
from random import randint


# Function inputs (parameters) are specified in the parentheses after the function name
#
# Here, f is the function name and it takes one input that is called x
# Function parameters are variables and use the same naming rules

def f(x):
    
    # return is the Python keyword to generate an output value from a function
    return 3 * x + 1


# Write a function to do g(x) = x ** 2 + 2 * x + 1
def g(x):
    return x ** 2 + 2 * x + 1


# Write a function to calculate area(r) = pi * r ** 2
def area(r):
    return pi * r ** 2


# Area of a rectangle -- functions can take any number of parameters
# separated by commas in the parentheses list
def area_of_rect(length, width):
    return length * width


# Max of two numbers
#
# Overrides the built-in max function
def max(a, b):
    if a > b:
        return a
    else:
        return b


# Min of two numbers
#
# Overrides the built-in min function
def min(a, b):
    if a < b:
        return a
    else:
        return b


# Test if an input number is odd
# Example of a function that returns a boolean result
def is_odd(n):
    if n % 2 == 1:
        return True
    else:
        return False
        

# Write a function that reads and returns an int from the terminal
def read_int():
    value = input('Enter an integer: ')
    value = int(value)
    return value


# A function to generate a random die roll -- six sided die
# use randint(1, 6) to generate a random value in [1, 6]
def six_sided_die():
    return randint(1, 6)


### Main -- statements outside of functions go here

a = area_of_rect(10, 5)
print(a)

m = max(.001, 101)
print(m)

radius = read_int()
a = area(radius)
print(a)

# An alternate way of doing the same calculation using function composition
print(area(read_int()))
