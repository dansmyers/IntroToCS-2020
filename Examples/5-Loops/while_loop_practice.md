# `while` Loop Practice

## Setup

```
cd CMS_195/Loops
```

Put each program in a separate file. You can pick the file names. Use `touch` to create each file and `open` to open it for editing.

## What's the Magic Word?

Write a loop that repeatedly prompts the user for input and runs until the user types the magic word `xyzzy`.

Tip: use a guard variable that is initially set to `True`. Use an `if` statement to test if the input is `xyzzy` and set 
`guard = False` if it is.

## Somebody Asked Me: Do I Smoke Meat?

Write a loop that prints `s m o k e t h e s e m e a t s` 1000 times.

## The Subtraction Game

Here's a mathematical strategy game that was played as a challenge on *Survivor: Thailand* where it was called Thai 21.

- Start with a pile of 21 stones.

- On her turn, a player may take 1, 2, or 3 stones from the pile.

- The player who takes the last stone is the winner.

Here is some starting code:

```
"""
The Subtraction Game (Thai 21 version)

CMS 195, Spring 2020

stones = 21
player = 1

playing = True

while playing:

    # Print the current player
    print("It's player %d's turn." % player)

    # Prompt the player to remove 1, 2, or 3 stones and read the input value
    
    # If the player enters 1, 2, or 3, update the number of stones
    
    # Else, print "You can't do that."
    
    # If there are 0 stones remaining, set playing = False
    
    # Else, switch to the other player
    
```

Interestingly, under these rules, there is a strategy that guarantees a win for the first player. Can you find it? Hint: if Player 2 begins a turn with four stones, is Player 1 guaranteed a win? What about if Player 2 begins with eight stones?

Thai 21 is a special case of the strategy game called Nim. In Nim, there are usually multiple piles of stones. Players are allowed to
take any number of stones, but from only one pile on each turn. In some variations, the player who takes the last stone **loses**.
