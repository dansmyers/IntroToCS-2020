"""
Echo program: print the user's input until the user types STOP

CMS 195, Spring 2020
"""

# "Guard variable" strategy

guard = True

# Loop executes as long as the guard variable is True
# Stops when guard becomes False

while guard:
    
    # Body of the loop
    value = input('Type something: ')
    print(value)
    
    # Test to determine if guard should become False and end the loop
    if value == 'STOP':
        guard = False
