"""
A common looping pattern: "accumulator" pattern

Loop over a range of numbers and use an additional variable to add them up

CMS 195, Spring 2020
"""

# Find the sum of the numbers from 1 to 100

n = 1
total = 0  # use total to keep track of the sum of the numbers (accumulates running sums)

while n <= 100:
    total = total + n
    n = n + 1
    
print(total)
