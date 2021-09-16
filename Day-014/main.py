# HIGHER - LOWER GAME

import random
from game_data import data
from art import logo
from art import vs
from clear_library import clear

keep_playing = True
score = 0
player1 = random.choice(data)
player2 = {}

def display_player(type, player):
    if(type == 1):
        print(logo)
        if(score > 0):
            print(f"You're right! Current score is: {score}.")
        print(f"Compare A: {player['name']}, a {player['description']} from {player['country']}")
    elif(type == 2):
        print(vs)
        print(f"Against B: {player['name']}, a {player['description']} from {player['country']}")
    else:
        print("ERROR. Something went wrong at 'display_player', please restart game.")

def check_answer(guess, player1, player2):
    if( (guess == "a" and player1['follower_count'] > player2['follower_count']) or (guess == "b" and player2['follower_count'] > player1['follower_count']) ):
        #User wins
        return "won"
    elif( player1['follower_count'] == player2['follower_count'] ):
        #draw
        return "draw"
    else:
        return "lose"


while(keep_playing == True):
    clear()

    #Display Player 1
    display_player(1, player1)

    #Display Player 2
    player2 = random.choice(data)
    display_player(2, player2)

    #Get input guess
    guess = input("Who has more followers? Type 'A' or 'B': ")

    #Check Answer
    result = check_answer(guess.lower(), player1, player2)

    #If user won: update player 1 and keep playing, else: finish game
    if(result == "lose"):
        keep_playing = False
        print(f"You lose. Your final score is: {score}")
    else:
        player1 = player2
        score += 1

