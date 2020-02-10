"""
A function can call another function!

What does this program print? What is the flow of execution?

CMS 195, Spring 2020
"""

def baz():
    print('In baz.')

def foo():
    print('In foo.')
    baz()  # Key idea: jump up and run baz's code and then come back to this point in the program
    print('Finished with foo.')
    
### Main
foo()
