import random
print("\n"
      "          __-----__\n"
      "     ..;;;--'~~~`--;;;..\n"
      "   /;-~IN GOD WE TRUST~-.\\\n"
      "  //      ,;;;;;;;;      \\\n"
      ".//      ;;;;;    \       \\\n"
      "||       ;;;;(   /.|       ||\n"
      "||       ;;;;;;;   _\      ||\n"
      "||       ';;  ;;;;=        ||\n"
      "||LIBERTY | ''\;;;;;;      ||\n"
      " \\\     ,| '\  '|><| 2022 //\n"
      "  \\\   |     |      \  A //\n"
      "   `;.,|.    |      '\.-'/\n"
      "     ~~;;;,._|___.,-;;;~'\n"
      "         ''=--'\n"
      "      Coin Flip Simulator\n"
      "\n")

repeat = True

while repeat is True:
    flip = input("Flip Coin? y/n ")
    if flip.lower() == "n":
        print("Thanks for playing!")
        repeat = False
        exit()
    else:
        sides = random.randint(0, 1)
        if sides == 1:
            print("Heads!")
        elif sides == 0:
            print("Tails!")



