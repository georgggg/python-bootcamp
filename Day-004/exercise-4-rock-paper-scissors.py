import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
options = ["rock", "paper", "scissors"]

user = input("Choose 'rock', 'paper' or 'scissors' to play: ").lower()
rnd = random.randint(0,2)
computer = options[rnd]
lose_msg = "You lose."
win_msg = "You won."
even_msg = "No one wins. We are even."

print("You chose")
if user == "rock":
    print(rock)
elif user == "paper":
    print(paper)
elif user == "scissors":
    print(scissors)

print("\n Computer chose: ")
if computer == "rock":
    print(rock)
elif computer == "paper":
    print(paper)
elif computer == "scissors":
    print(scissors)


if(user == "rock"):
    if computer == "paper":
        print(lose_msg)
    elif computer == "scissors":
        print(win_msg)
    else:
        print(even_msg)
elif user == "paper":
    if computer == "rock":
        print(win_msg)
    elif computer == "scissors":
        print(lose_msg)
    else:
        print(even_msg)
elif user == "scissors":
    if computer == "rock":
        print(lose_msg)
    elif computer == "paper":
        print(win_msg)
    else:
        print(even_msg)
else:
    print("Your input was not understood, please try again.")