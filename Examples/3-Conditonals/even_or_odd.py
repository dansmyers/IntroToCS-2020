"""
Test if a number is even or odd

CMS 195, Spring 2020
"""

# Read a number
number = int(input('Enter a number: '))

# Use the % operator to test the remainder after division

# if-else is used for mutually exclusive choices
# One branch or the other must occur

# If the first test is True, the code inside the if block executes
# If the first test is False, the code inside the else block executes

if number % 2 == 0:
    print('Even')
else:
    print('Odd')
