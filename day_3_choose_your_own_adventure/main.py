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
finished_game = False
while finished_game is False:  # allows for process to repeat. Keep this on main menu always
    print("                       ", "\nWelcome to Treasure Island.")  # new line; space to make text more readable
    print("Your mission is to find the treasure.")
    entrance = input("Left or Right? ")

    if entrance.lower() != "left":
        print("You fell into a hole, game over.")
    else:
        swim_or_wait = input("Swim, or Wait? ")
        if swim_or_wait.lower() != "wait":
            print("You were attached by a trout. Game Over.")
        else:
            door_choice = input("Which door, Red, Yellow, Or Blue?")  # dead ends going first
            if door_choice.lower() == "red":
                print("You were burned by fire. Game Over.")
            elif door_choice.lower() == "blue":
                print("You were eaten by beasts. Game Over.")
            elif door_choice.lower() != "yellow":
                print("Game Over.")
            elif door_choice.lower() == "yellow":
                print("You win!")
                restart = input("start over? y/n ")
                if restart.lower() != "y":  # instead of just if y if n, if it's not expressly yes then its no
                    finished_game = True
                else:
                    pass
