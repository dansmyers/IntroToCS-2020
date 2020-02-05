"""
An implementation of the world's least supportive therapist

CMS 195, Spring 2020
"""

# This program illustrates the use of the if statement

# Prompt the user to pick one of two options
# Based on the user's choice, print a supportive message

# Prompt the user with some options
print('How are you feeling today?')
print('1. Pretty good.')
print('2. Not so great.')

# Read the user's response
response = input('Enter your choice: ')

# Convert the string response to a number
response = int(response)

# Make a decision based on the user's input
if response == 1:
    print('Sounds good. Keep up the great work.')

# A second if statement for the other choice
if response == 2:
    print('I hope things get better.')
    
# Thought: the options are mutually exclusive. Can we write this another way?
