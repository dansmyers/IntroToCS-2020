"""
Magic Eight Ball: a fortune telling program

CMS 195, Spring 2020
"""

from math import random

# Read a question from the user
# This is just for flavor: it has no effect on the output
print('I AM THE MAGIC EIGHT BALL!")
question = input('Tell me your question: ')

# Generate a random number in [0, 1)
r = random()

# Use the value of r to select an output message
if r <= .25:
    print('My sources say no.')
elif r > .25 and r <= .50:
    print('It is decidedly so.')
elif r > .50 and r <= .75:
    print('Concentrate and ask again.')
else:
    print('Signs point to yes.')
