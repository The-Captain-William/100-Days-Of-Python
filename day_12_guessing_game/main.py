import random
# took me 19 mins to make and completed and polished 1 hour 20 mins ish after bug fixing


def high_or_low(number, guess, lives):
    if number > guess and lives > 0:
        print("\nToo low")
        print("Try again")
        return False
    elif number < guess and lives > 0:
        print("\nToo high")
        print("Try again")
        return False
    elif number == guess:
        print("\nYou win!")
        return True
    if lives < 0:  # this will not check here but safety measure
        return True


print("Captain William Presents: Guessing Game")

new_game = True  # new game start, refresh
loop = True
while new_game is True:
    player_guesses = []
    player_lives = 5
    number = random.randint(1, 100)
    easy_or_hard = input("Easy, or Hard?: ").lower()
    if easy_or_hard == 'easy':
        player_lives += 5
        print(f"Player Lives: {player_lives}")
    elif easy_or_hard == 'hard':
        print(f"Player Lives: {player_lives}")

    if easy_or_hard == 'easy' or easy_or_hard == 'hard':
        new_game = False
        loop = True
    else:
        new_game = True
        print("Invalid")
        loop = False

    while loop is True:  # loop for getting incorrect values
        player_guess = int(input("Pick a number from 1 to 100: "))
        game = high_or_low(number, player_guess, player_lives)
        if game is False:
            player_lives -= 1
            player_guesses.append(player_guess)
            print(f"\nPlayer Lives: {player_lives} \nWrong Guesses: {player_guesses}")
        elif game is True:
            loop = False  # loop is terminated when won or game lost
        if player_lives <= 0:
            loop = False
            print(f"\nYou lose!, the number was {number}")

    while loop is False:  # when loop is terminated, menu activated
        repeat = input("\nTry again? y/n ").lower()
        if repeat == "y":
            new_game = True
            loop = True
        elif repeat == "n":
            print("Thank you for playing!")
            exit()
        else:
            print("Invalid")











