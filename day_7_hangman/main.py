import random
from stage_number import stage_number
from word_list import word_list

#word_list = ["aardvark","baboon", "camel"]
blanks = []
incorrect_letters = []
correct_letters = []
play = True



lives = 6
print("Welcome to hangman!")
title_screen = """
888                                                           
888                                                           
888                                                           
88888b.  8888b. 88888b.  .d88b. 88888b.d88b.  8888b. 88888b.  
888 "88b    "88b888 "88bd88P"88b888 "888 "88b    "88b888 "88b 
888  888.d888888888  888888  888888  888  888.d888888888  888 
888  888888  888888  888Y88b 888888  888  888888  888888  888 
888  888"Y888888888  888 "Y88888888  888  888"Y888888888  888 
                             888                              
                        Y8b d88P                              
                         "Y88P"           
"""
stage_number(lives)
print(title_screen)
hint_attempt = 2

while play is True:
    word_select = random.choice(word_list)  # pick a word
    for char in word_select:
        blanks += "_"
    is_guessing = True


    while is_guessing is True:
        player_guess = input("Pick a letter (or 'exit' to exit): ").lower()  # exit, start
        print(incorrect_letters)
        if player_guess.lower() == "exit":
            exit()

        for word in word_list:
            if player_guess.lower() != word_select:
                if player_guess == word: # word w.r.t entire dictionary
                    print("Incorrect word, you lose!")  # terminate game with loss, wrong word
                    lives = 0
                    pass
                    break

        if len(player_guess) > 1 and player_guess.lower() != word_select:  # only one character at a time TODO [word or character not in list, or too many letters]
            print("only one character at a time, unless you know the word!")
            break
            pass

        if len(player_guess) > 1 and player_guess.lower() == word_select:
            blanks.clear()
            for char in word_select:
                blanks.append(char)
            stage_number(lives)
            print(f"{''.join(blanks)}")
            print("You win!")
            print(f"Incorrect Letters: {incorrect_letters}")
            is_guessing = False

        for position in range(len(word_select)):  # iterating through selected word
            char = word_select[position]  # defining char to be item in word_select at index [position]
            if char == player_guess.lower():
                blanks[position] = char

        for char in word_select:
            if player_guess in word_select:
                if player_guess in correct_letters:
                    stage_number(lives)
                    print(f"{''.join(blanks)}")
                    print(f"Incorrect Letters: {incorrect_letters}")
                    print(f"You have selected the letter {player_guess} already")
                    break
                if player_guess not in correct_letters:
                    stage_number(lives)
                    print(f"{''.join(blanks)}")
                    print("Correct!")
                    print(f"Incorrect Letters: {incorrect_letters}")
                    correct_letters.append(player_guess)
                    break

        # define a variable number in the range of the length of the word
        # explicitly define the value char to be equal to the value of word select at that index position
        # we are explicitly defining char to be a value of word, and explicitly defining position to reference
        # the index number at the same time, mapping them together.
        # list at index position [position] becomes that character

        if player_guess not in word_select:  # check to see if player guess value is equal to ANY value in word select
            if player_guess in incorrect_letters:
                stage_number(lives)
                print(f"{''.join(blanks)}")
                print(f"Incorrect Letters: {incorrect_letters}")
                print(f"You have selected the letter {player_guess} already ")
            elif player_guess not in incorrect_letters:
                lives -= 1
                stage_number(lives)
                print(f"{''.join(blanks)}")
                print("Incorrect!")
                incorrect_letters.append(player_guess)
                print(f"Incorrect Letters: {incorrect_letters}")

        if lives == 0:
            stage_number(lives)
            print("You lose!")
            print(f"The correct answer was: {word_select}")
            is_guessing = False

        if "_" not in blanks:
            stage_number(lives)
            print(f"{''.join(blanks)}")
            print(f"Incorrect Letters: {incorrect_letters}")
            print("You win!")
            is_guessing = False  # catch-all incase user enters character-by-character and not entire word

        if lives < 2 and "_" in blanks:
            if hint_attempt > 0:
                hint = random.choices(word_select, k=2)
                print(f"Hint: {hint[0]} and {hint[1]}")
                hint_attempt -= 1

    while is_guessing is False:
        play_again = input("Play again? y/n: ").lower()
        if play_again == "y":
            play = False
            blanks.clear()
            lives = 6
            hint_attempt = 2
            incorrect_letters.clear()
            correct_letters.clear()
            if play is False:  # switch
                play = True
                is_guessing = True
                print(title_screen)
        elif play_again == "n":
            print(title_screen)
            print("Thanks for playing!")
            play = False
            exit()
        else:
            print("Incorrect key")  # loop to prevent game from replaying if incorrect
            play_again = False








