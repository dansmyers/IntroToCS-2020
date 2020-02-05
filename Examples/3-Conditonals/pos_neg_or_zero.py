"""
Test if a number is positive, negative, or zero

CMS 195, Spring 2020
"""

# Read the number
number = int(input('Enter a number: '))

# This test block has three outcomes
#
# Use if-elif-else to test three or more outcomes

# If the first test is True, the if block executes and all of the other cases are skipped
#
# If the first test is False, the elif test is checked. If that test is True, the elif block executes
#
# If both tests are False, the else block executes as the default outcome

# You can add any number of elif clauses to test more than three outcomes
# There can be only one final else block

if number > 0:
    print('Positive')
elif number < 0:
    print('Negative')
else:
    print('Zero')
