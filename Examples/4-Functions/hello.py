"""
Is it me you're looking for?

Say hello 100 times

The best way to solve this problem is to use a loop, but
let's think about how to do it efficiently using functions

CMS 195, Spring 2020
"""

# Define a function that prints hello
def hello():
    print('Hello!')
    
# Define a function that prints hello five times
def hello_five_times():
    hello()
    hello()
    hello()
    hello()
    hello()
    
# Define a function that prints hello 25 times
def hello_25_times():
    hello_five_times()
    hello_five_times()
    hello_five_times()
    hello_five_times()
    hello_five_times()

# Define a function that prints hello 100 times
def hello_100_times():
    hello_25_times()
    hello_25_times()
    hello_25_times()
    hello_25_times()

### Main
hello_100_times()
