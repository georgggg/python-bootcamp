from clear_library import clear
#HINT: You can call clear() to clear the output in the console.
from art import logo

print(logo)

keep_going = True
bids = {}
winner = ""
winning_amount = 0

while keep_going == True:
	name = input("What is your name? ").lower()
	bid = float(input("What is your bid? $"))
	
	bids[name] = bid
	
	choice = input("Type 'yes' to register more bids or 'no' to stop accepting bids ").lower()
	
	if choice == "yes":
		clear()
	elif choice == "no":
		keep_going = False
	else:
		print("You provided an invalid input, I am finishing the auction now.")
		keep_going = False


for key in bids:
	if bids[key] > winning_amount:
		winner = key
		winning_amount = bids[key]

if winning_amount == 0:
	print("No one wins this auction")
else:
	print(f"{winner} won this auction with a bid of ${winning_amount}")
