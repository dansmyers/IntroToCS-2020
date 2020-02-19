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
    print('But you need to head back to your house before you do anything else.')
    
    # Go directly to the next page without offering a choice
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
        print()
        print('Congratulations! You made back to your house!')
        print('If only there was some way to get inside...')
        print()
    else:
        print()
        print('Opening the mailbox reveals a small leaflet.')
        print()
        
        print('1. Read the leaflet.')
        print('2. Change your mind and go to the house.')
        
        choice = int(input('Make a choice: '))
        
        if choice == 1:
            print()
            print('The leaflet turns out to be a coupon for a nearby all-you-can-eat Chinese buffet.')
            print('Your stomach rumbles...')
            print('But you need to head back to your house before you do anything else.')
            
            # Go directly to the next page without offering a choice
            go_to_house()
        else:
            go_to_house()
        
        
def print_instructions():
    
    print('Welcome to my Choose Your Own Adventure story!')
    print()
    
    print('Every page in this book is implemented as a function.')
    print('On each page, you\'ll make a choice, which calls the next function.')
    print('Let\'s begin!')
        
        
### Main
print_instructions()
start()
