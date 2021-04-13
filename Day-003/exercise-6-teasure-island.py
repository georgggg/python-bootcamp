print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.") 

#https://www.draw.io/?lightbox=1&highlight=0000ff&edit=_blank&layers=1&nav=1&title=Treasure%20Island%20Conditional.drawio#Uhttps%3A%2F%2Fdrive.google.com%2Fuc%3Fid%3D1oDe4ehjWZipYRsVfeAx2HyB7LCQ8_Fvi%26export%3Ddownload


choice1 = input("You are at a crossroad. If you have the courage to start an adventure then open the 'red' door, otherwise open the 'black' door.").lower()

if choice1 == "red":
    print("<> Welcome to your custom adventure.")
    choice2 = input("You are at a dock and you can take a 'boat' or a 'plane' to start your adventure.").lower()
    if choice2 == "plane":
        print("Your plane crashed. Game Over!")
    else:
        choice3 = input("You arrived to a beach in the south side of the treasure island. How will you search for the treasure? 'swim' or 'dig'").lower()
        if choice3 == "swim":
            print("You drowned. Game over!")
        elif choice3 == "dig":
            choice4 = input("You chose to dig. Specify where you will start digging: 'south', 'north', 'east' or 'west'").lower()
            if choice4 == "south":
                print("You didn't find the treasure and you must take the boat to go back home alive before dawn. Game over!")
            elif choice4 == "north":
                print("You walked to north and digged. While you were digging a group of locals found you making holes on the ground and killed you. Game over!")
            elif choice4 == "west":
                print("You walked all the way to the end of the island on the west side, then you fell off a cliff and died. Game over!")
            elif choice4 == "east":
                print("You searched for 3 hours and finally you found the")
                print('''_                                     
                        | |                                    
                        | |_ _ __ ___  __ _ ___ _   _ _ __ ___ 
                        | __| '__/ _ \/ _` / __| | | | '__/ _ \
                        | |_| | |  __/ (_| \__ \ |_| | | |  __/
                         \__|_|  \___|\__,_|___/\__,_|_|  \___|''')
                print("You can now go back south, take the boat and bring the treasure back home. You won this game.")
            else:
                print("It seems like you don't know how to follow instructions. This way it is not possible to find the treasure. Game over!")
        else:
            print("You chose something else. Game over!")
else:
    print("You chose not to have an adventure. Come back when you are ready to leave your comfort zone.")
