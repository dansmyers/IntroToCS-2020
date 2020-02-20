# WRITE ALL THE FUNCTIONS!

<img src="https://wompampsupport.azureedge.net/fetchimage?siteId=7575&v=2&jpgQuality=100&width=700&url=https%3A%2F%2Fi.kym-cdn.com%2Fentries%2Ficons%2Ffacebook%2F000%2F006%2F199%2Fresponsibility12(alternate).jpg" width="50%"/>

## Chuck-a-Luck

An old-time carnival game.

The player bets on a number 1 through 6 and then rolls three dice.

- If the number comes up one time the player wins $1.
- If it comes up two times the player wins $2.
- If it comes up three times the player wins $3.

Here is some starter code. Fill in the methods.

```
"""
Chuck-a-Luck

CMS 195, Spring 2020
"""

from random import randint

def read_int():
    """
    Read and return an integer from the terminal
    """
    
    # Write code to read a value with input(), then convert it to an int and return it
    
  
def die_roll():
    """
    Generate and return a six-sided die roll
    """
    
    # Fill in the body of the method


def print_instructions():
    """
    Instructions for the chuck-a-luck game
    """
    
    # Print instruction messages for the user
    # This method doesn't return anything
    
    
### Main
    
print_instructions()

# Read the user's bet
bet = read_int()

# Generate three dice
die1 = die_roll()
# Use die_roll() to initialize variables die2 and die3
    
# Count up the number of dice that match the user's bet
# Tip: create a count variable and test each die with an if statement

# Print the outcome

```

## You Will Find True Love on Flag Day

Take a look at the following flag design:

```
+--+--+--+--+--+
+**+  +**+  +**+
+**+  +**+  +**+
+--+--+--+--+--+
+  +**+  +**+  +
+  +**+  +**+  +
+--+--+--+--+--+
+**+  +**+  +**+
+**+  +**+  +**+
+--+--+--+--+--+
```

Can you write a group of functions that will print this flag? Try to use the minimum number of individual `print` statements in your program.

Tip: it's easy to write functions that print entire lines, but can you take advantage of the repeating patterns to break things down more?

## Would Everyone Please Rise for the Presentation of Our National Colors

Design your own **sweet** text flag and write a program that uses methods to print it.

Again, try to minimize the number of individual `print` statements in your code and try to break things down to the finest level of detail possible.

[Proposal to update the Rollins Alma Mater](https://www.youtube.com/watch?v=fiyL-bKwL4U).


## Binet's Formula
Recall Binet's formula from assignment 2: it gives a closed-form way of calculating the Fibonacci numbers.

```
F_n = (1 / sqrt(5)) * (phi ** n - phi_hat ** n)
```

Where `phi` is the special **golden ratio**:

```
phi = (1 + sqrt(5)) / 2

phi_hat = (1 - sqrt(5)) / 2
```

Write a function called `binet` that takes a parameter `n` as input and uses it to calculate and return the `n`th Fibonacci number. Write 
some code in the main part of your program to test your function.

## One-Armed Bandit

Write a slot machine program.

- Generate three random numbers in the range 0 to 9.
- If all three numbers are the same, print `Jackpot!`.
- If two of the three are the same, print `Winner!`.

Design your own functions for this program. Look at the chuck-a-luck game as a template. You don't need to prompt the user for any input.

