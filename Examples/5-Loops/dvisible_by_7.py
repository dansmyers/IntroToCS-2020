"""
A second common pattern: combine a loop with an if statement

General idea: loop over a range and select only certain values to process

CMS 195, Spring 2020
"""

# Print numbers less than 100 divisible by 7

n = 1

while n < 100:
    
    if n % 7 == 0:
        print(n)
    
    n = n + 1
