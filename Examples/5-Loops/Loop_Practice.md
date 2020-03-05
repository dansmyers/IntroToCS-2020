# Loop Practice

## Tower of Power

Write a program that uses a `for` loop to print a tower like the following. The tower is 20 lines high and each line has 10 `#` symbols.

```
##########
##########
##########
##########
##########
##########
##########
##########
##########
##########
##########
##########
##########
##########
##########
##########
##########
##########
##########
##########
```

Now modify your program to define a function called `tower` that takes a parameter called `height`:

```
def tower(height):
    """
    Print a tower with height rows.
    
    Parameter
    ---------
    height (int): the number of rows in the tower
    """
```

Complete the method with a loop that prints `height` rows of ten blocks each.

## Super Pyramid

Write a program with a function named `pyramid` that takes a parameter named `height` and prints a pyramid like the following:

```
    *
   * *
  * * *
 * * * *
* * * * *
```

Tip:

Row 1 has `height - 1` spaces followed by one `* ` (that's a star and space). Row 2 has `height - 2` spaces followed by two `* `.

```
def pyramid(height):
    """
    Print a pyramid.
    
    Parameter
    ---------
    height (int): the number of levels in the pyramid.
    """

    # Use an outer for loop to iterate over the number of rows
    
    
        # Use an inner for loop to print spaces
        
        
        # Use a second inner for loop to print '* ' strings
```

## Babylonian Square Roots

We've touched a few times on the question of how computers can do complex mathematical calculations like square roots.

Here's an ancient algorithm for determining the square root of a given number `n`. It's commonly known as the Babylonian method,
although there's no direct evidence that the Babylonians actually used it. It was definitely known and described by the Greeks in the
early First Century A.D.

Suppose we want to find the square root of a number `n`. Let `x` be an initial guess of the square root. Picking a good initial guess
is nice but not required.

The method repeatedly calculates a new, better estimate using the rule:

```
x = .5 * (x + n / x)
```

For example, suppose `n` = 121 and `x` = 1.

```
.5 * (1 + 121 / 1) = 61

.5 * (61 + 121 / 61) = 31.4918

.5 * (31.4918 + 121 / 31.4918) = 17.6670

.5 * (17.6670 + 121 / 17.6670) = 12.2579

.5 * (12.2579 + 121 / 12.2579) = 11.0645

.5 * (11.0645 + 121 / 11.0645) = 11.0001
```

The method has basically converged to the true square root after only six update steps.

Why does it work?

Intuitively, if `x` is **smaller** than the real square root, then `n / x` must be **bigger** than the real square root. Therefore,
their average should be an improved estimate. The same logic applies if `x` is bigger than the true root. Therefore, the Babylonian
algorithm just repeatedly calculates the average of `x` and `n / x` and uses that as the new value of `x` in
the next iteration.

Write a program that uses the Babylonian method in a `for` loop to find the square root of 603729 starting from a guess of 1.
Print the value of `x` on each iteration of the loop. How many iterations are required for the method to converge?

## Advanced Snow Cone Truck

Here's another useful loop technique: forcing a user to give you valid input.

Recall the snow cone truck example from a while back.

```
"""
Abominable Snow Cone Truck

CMS 195, Spring 2020
"""

print('Welcome to the Snow Cone Truck!')
print('1. Cherry')
print('2. Blue Raspberry')
print('3. Tiger Blood')
print('4. Horchata')

flavor = int(input('Choose a flavor: `))

if flavor < 1 or flavor > 4:
    print(That\'s not a choice!')
    quit()
    
else:
    print('Enjoy your cone!')
```

Let's modify this program so the user has to enter a number 1-4. Use a `while` loop that wraps around the input reading step. After
reading the input, check if it's between 1 and 4. If so, end the loop. If not, print an error message and keep looping.

```
looping = True  # Loop control variable

while looping:

    flavor = int(input('Choose a flavor:'))
    
    if 1 <= flavor <= 4:
        looping = False  # If the input is valid, set looping to False to end
    else:
        print('Sorry, that\'s not an option. Try again.')
```

Rewrite the original program to replace the `if`-`else` block with the `while`-based input collection step. Verify that the updated
code works correctly.


## If They're the Mario Brothers, Does That Mean His Name is Mario Mario?

At the end of each level in the original *Super Mario Bros.*, Mario jumps up stairs like the following:

```
     ##
    ###
   ####
  #####
 ######
#######
```

Write a program with a function called `mario_stairs` that takes a parameter `height` as input and prints the appropriately-sized
Mario-style stairs.

```
def mario_stairs(height):
    """
    Print Mario-style stairs.
    
    Parameter
    ---------
    height (int) : the number of levels in the staircase
```

Tip:

The first level has `height - 1` spaces and two blocks. The second level has `height - 2` spaces and three blocks. Use an outer `for`
loop over the number of rows and then two inner `for` loops: one for the spaces and a second one for the blocks.


## Fibonacci

Recall the famous Fibonacci sequence, where each number is the sum of the two previous Fibonacci numbers:

1, 1, 2, 3, 5, 8, 13, 21, 34, 55, ...

Write a program that uses a `for` loop to calculate and print the first 50 Fibonacci numbers.

```
prev = 0
current = 1

# Use a for loop that runs for 50 iterations

    # Inside the loop, print the current Fibonacci number
    
    # Calculate the next Fibonacci number
    next = current + prev
    
    # Set prev = current and current = next to advance forward by one number

```

Now modify your program to use a method called `fib` that takes a parameter `n` as input and **returns** the `n`th Fibonacci number.

```
def fib(n):
    """
    Calcuate and return the nth Fibonacci number -- assume n > 1
    """
    
    prev = 0
    current = 1

    # Use a for loop that runs for n iterations

        # Calculate the next Fibonacci number
        next = current + prev

        # Set prev = current and current = next to advance forward by one number

    return current

### Main
print(fib(5))
print(fib(10))
```


## Baby Needs a New Pair of Shoes

**This problem is on Assignment 6. Completing it will give you an example that will help with the other two simulation problems.**

What is the average value obtained by rolling two dice?

One way to solve this problem is to reason about the underlying probabilities. Another way is to simply **simulate** a large number
of dice rolls and calculate the average from the simulated results. With high probability, the simulated average should be a close
approximation of the true average.

This type of program is called a **Monte Carlo simulation**, named after the famous Monte Carlo casino complex in the tiny
European principality of Monaco.

Fill in the `main` of the program below. Use a `for` loop to call `simulate` 1000 times and add up the results of all the simulated
die rolls. At the end of the program, calculate the average over all 1000 trials.

```
"""
Simulate the average of rolling two dice

CMS 195 Spring 2020
"""

from random import seed, randint

def simulate():
    """
    Roll two dice and return their sum
    """
    
    # Fill in the body of this method
    # Generate two random die rolls and return their sum
    

### Main

seed(0)  # DON'T MODIFY THIS LINE

total = 0

# Use a for loop that runs for 1000 trials

    # Inside the loop, call simulate and add the value it returns to the running total


# Print the average of all 1000 simulations
print(total / 1000)
```

## Ultimate RPS

Let's update the rock-paper-scissors game to play best two out of three and allow the user to play multiple games.

Take a look at the starting code below and fill in the missing pieces.

```
"""
Ultimate RPS

CMS 195, Spring 2020
"""

from random import randint

def play_rps():
    """
    Play one round of RPS.
    
    Returns
    -------
    'draw' if the players draw
    'player' if the player wins
    'cpu' if the cpu wins
    """
    
    ROCK = 1
    PAPER = 2
    SCISSORS = 3
    
    print('1. Rock')
    print('2. Paper')
    print('3. Scissors')
    
    getting_input = True
    while getting_input:
        player_move = int(input('Choose your move: '))
    
        # TODO: Test if the player move is valid
        # If it is, set getting_move = false
        # If it isn't, print an error message and keep looping
 
    # Choose a random computer move
    cpu_move = randint(1, 3)
    
    if cpu_move == ROCK:
        print('I rock.')
    
    # TODO: Add two more cases for the other CPU moves
    
    # TODO: Test for a draw. If both moves are the same return 'draw'
    
    # TODO: Test for the winner
    #
    # If the player wins, return `player`
    # If the computer wins, return `cpu`
    
    return player
    

def play_best_two_of_three():
    """
    Play RPS until either the player or CPU wins two games
    
    Most of the work is in the play_rps method, which returns a string naming the winner
    """
    
    player_wins = 0
    cpu_wins = 0
    
    while player_wins < 2 and cpu_wins < 2:
        
        # TODO: Print the current score for the player and computer
        
        print('Ready? FIGHT!')
    
        winner = play_rps()
        
        if winner == 'player':
            player_wins += 1
        elif winner == 'cpu':
            cpu_wins += 1
            
    if player_wins == 2:
        print('You are the supreme champion.')
    else:
        print('Resistance is futile.')
        
        

def game():
    """
    The main game loop: play one round, then prompt the user to continue or not
    """
    
    playing = True
    
    while playing:
        play_best_two_of_three()
        
        response = input('Do you want to play again (Y / N)? ')
        
        if response == 'N':
            playing = False

### Main
game()
game()
```
