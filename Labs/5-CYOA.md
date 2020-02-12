# Choose Your Own Adventure

## Description

If you had been a kid in the 80's, your elementary school library would have been stuffed with *Choose Your Own Adventure* books, for the downtime you had when you weren't playing [*Oregon Trail*](https://en.wikipedia.org/wiki/The_Oregon_Trail_(1985_video_game)) on your school's Apple II computers.

![](https://upload.wikimedia.org/wikipedia/en/f/f0/Cave_of_time.jpg)

Each book was the story of "you", the nameless protagonist, making your way through some type of fantastic adventure story. After reading for a few pages, you'd be offered a choice:

- *If you choose to explore the mysterious Cave of Time, turn to page 41*.

- *If you would rather go back to your house and make a sandwich, go to page 17*.

Each choice would lead to a different path of the story and eventually you would reach an ending page, which might good, bad, or curiously ambiguous.

The CYOA books are part of the larger gaming lineage of **interactive fiction**. Some of the earliest PC games were structured as interactive stories, where the player types commands to move around the world, gather items, and solve puzzles. These early text-based IF games later evolved into graphical adventure games.

![](https://upload.wikimedia.org/wikipedia/en/a/ac/Zork_I_box_art.jpg)

We're going to use Python to write our own text-based Choose Your Own Adventure story. A key idea of this program will be **using functions to organize a complex program**.

- Each "page" of the story will be its own function. Within each function, print a little descriptive text, then prompt the user to make a choice.

- Each choice corresponds to another function call, which runs the code for the next page.

## Example

### Setup

```
cd CMS_195/Functions
```

```
touch cyoa.py
```

```
open cyoa.py
```

### Some Starter Code

Put the following code in your `cyoa.py` file, then run it a couple of times to see how it works.

```
"""
A Choose Your Own Adventure Story, featuring functions

CMS 195, Spring 2020
"""

def go_to_house():
    
    print()
    print('Congratulations! You made back to your house!')
    print('If only there was some way to get inside...')
    print()
    
    # Add some more choices
    # Each choice corresponds to a function that represents the next page in the story
   
   
def read_leaflet():

    print()
    print('The leaflet turns out to be a coupon for a nearby all-you-can-eat Chinese buffet.')
    print('Your stomach rumbles...')
    print()
    
    print('1. Drive to the buffet.')
    print('2. Go to your house.')
        
    choice = int(input('Make a choice: '))
    
    if choice == 1:
        drive_to_buffet()
    else:
        go_to_house()

    
def open_mailbox():
    
    print()
    print('Opening the mailbox reveals a small leaflet.')
    print()
    
    print('1. Read the leaflet.')
    print('2. Change your mind and go to the house.')
    
    choice = int(input('Make a choice: '))
    
    if choice == 1:
        read_leaflet()
    else:
        go_to_house()
        

def start():
    
    print()
    print('You are standing in an open field west of a white house with a boarded front door. There is a small mailbox here.')
    print()
    
    print('1. Go to the house.')
    print('2. Open the mailbox.')
    
    choice = int(input('Make a choice: '))
    
    if choice == 1:
        go_to_house()
    else:
        open_mailbox()
        
        
def print_instructions():
    
    print('Welcome to my Choose Your Own Adventure story!')
    print()
    
    print('Every page in this book is implemented as a function.')
    print('After reading each page, you\'ll make a choice, which calls another function to take you to the next page.')
    print('Let\'s begin!')
        
        
### Main
print_instructions()
start()
```

