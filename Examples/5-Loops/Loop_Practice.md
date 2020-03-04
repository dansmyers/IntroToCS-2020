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
