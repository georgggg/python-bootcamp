#Number Guessing Game Objectives:

# Include an ASCII art logo.
# Allow the player to submit a guess for a number between 1 and 100.
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer. 
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player. 
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).

import random
from art import logo
from clear_library import clear

LOWER_LIMIT = 1
HIGHER_LIMIT = 100
EASY_CHANCES = 10
HARD_CHANCES = 5
keep_playing = True

def check_guess(current_number,guess):
    if guess > current_number:
        print("Your answer if too high")
        return 0
    elif guess < current_number:
        print("Your answer if too low")
        return 0
    elif (current_number == guess):
        print(f"Your answer is right. The number is: {current_number}")
        return 1
    else:
        print("ERROR. Please restart this game")
        return -1


while(keep_playing):
    clear()
    print(logo)
    enter_game = input("Write 'y' to play 'Guess the Number': ")
    if(enter_game.lower() == 'y'):
        current_number = random.randint(LOWER_LIMIT, HIGHER_LIMIT)
        game_mode = input(f"Write 'e' for easy mode ({EASY_CHANCES} chances) or 'h' for hard mode ({HARD_CHANCES} chances): ")
        
        if(game_mode.lower() == 'h'):
            mode = HARD_CHANCES
        else:
            mode = EASY_CHANCES
        
        while(mode > 0):
            guess = input(f"Write a number between {LOWER_LIMIT} and {HIGHER_LIMIT} ({mode} chances left): ")
            result = check_guess(current_number, int(guess) )
            
            if(result == 1):
                input("Press Enter to continue... ")
                break

            mode -= 1
            if(mode == 0):
                input(f"You ran out of chances. The number was {current_number} Press Enter to continue...")
    else:
        keep_playing = False

