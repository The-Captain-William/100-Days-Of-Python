import random

print("""                       (
                        )     (
                 ___...(-------)-....___
             .-..       )    (          ..-.
       .-'``'|-._             )         _.-|
      /  .--.|   `..---...........---..`   |
     /  /    |                             |
     |  |    |                             |
      \  \   |                             |
       `\ `\ |                             |
         `\ `|                             |
         _/ /\                             /
        (__/  \                           /
     _..---..` \                         /`..---.._
  .-'           \                       /          '-.
 :               `-.__             __.-'              :
 :                  ) ..---...---.. (                 :
  '._               `.--...___...--.`              _.'
    \..--..__                              __..--../
     '._     ...----.....______.....----...     _.'
        `..--..,,_____            _____,,..--..`
                      `...----...` 
                    Banker's Roulette 
                      """)

repeat = True
while repeat is True:
    names = input("Give me the names of everyone, separated by a comma, or type esc to exit: ").split(", ")
    if names[0].lower() != "esc" and repeat != False:  # a list is still generated so we pick index zero.  !=False is kind of redundant here but still.
        print(f"{random.choice(names)} is going to pay the bill today!")
        start_over = input("repeat? y/n: ")
        if start_over == "n":
            repeat = False
            pass
    else:
        repeat = False

while repeat is False:
    print("Thanks for playing!")
    exit()

