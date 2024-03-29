# This was re-written in Python based on the JavaScript version within this GitHub repository.

# Import modules
import math
import random

# Print welcome message
print ("Welcome to Battleship!")

# Define function
def battleship():
    # Declare variables
    randomLoc = math.floor(random.randint(0,8))
    location1 = randomLoc
    location2 = location1 + 1
    location3 = location2 + 1
    guess = 0
    hits = 0
    guesses = 0
    isSunk = False

    # Main loop
    while isSunk == False:
        guess = int(input("Ready, aim, fire! Enter a number 0-10:"))
        if guess < 0 or guess > 10 :
            print ("Please enter a valid cell number!")   
        else: 
            guesses = guesses + 1
            if guess == location1 or guess == location2 or guess == location3:
                hits = hits + 1
                print ("HIT!")
            elif guess != location1 or location2 or location3:
                print ("MISS")
            if hits == 3:
                isSunk = True
                print ("You sank my battleship!")

# Call function
battleship()

# Declare playAgain variable
playAgain = 0

# Play again loop
while playAgain != "n":
    print("Play again? y/n")
    playAgain = input()
    if playAgain == "y":
        battleship()
