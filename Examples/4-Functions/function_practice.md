# Function Practice

## Setup

```
cd CMS_195/Functions
```

```
touch function_practice.py
```

```
open function_practice.py
```

Here is some starter code for your file:

```
"""
Practice writing functions that return values

CMS 195, Spring 2020
"""

from random import randint


### Declare functions in this section




### Main -- statements outside of functions go here


```

## Questions

### Coin Flip
Write a function called `flip` that simulates a coin flip by returning a randomly chosen value of 0 or 1.

### Roll

Write a function called `d20` that simulates the roll of a 20-sided die by returning a random value in [1, 20].

### Two Dice

Write a function called `roll_two_dice` that returns the sum of rolling two six-sided dice.

### 7 Come 11

Craps is the most popular dice game in American casinos. Several craps bets revolve around the numbers 7 or 11.

Write a function called `is_7_or_11` that takes an input and returns `True` if the value is 7 or 11 and `False` otherwise.

```
def is_7_or_11(roll):

    # Fill in the function body
```

### Live and Let Die

Write a function called `n_sided_die` that takes a parameter `n` as input and simulates rolling an `n`-sided die by returning a random
value in the range [1, `n`].
