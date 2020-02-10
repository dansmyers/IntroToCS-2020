"""
Our first example of a function: use a function to print a message

CMS 195, Spring 2020
"""

def print_message():
    print()  # Blank line
    print('This message is being printed by the function.')
    print('These lines print every time you call print_message.')
    print()  # Blank line
    

### Main
print('This line prints before calling print_message.')

print_message()

print('This line prints after calling print_message.')
