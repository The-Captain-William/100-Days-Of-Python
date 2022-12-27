from art import logo
from higher_or_lower import data
import random


# count = data[0]["follower_count"]  # data is a list of dictionaries; example
# completed in 1 hour 57 minutes

def call_followers():  # function to select two dictionaries from the list of dictionaries
    global choice_1  # global variables so other functions can interact
    global choice_2
    global choices
    no_repeat = True
    while no_repeat is True:  # will keep selecting choices until both choices are not equal
        choices = random.choices(data, k=2)  # random selection
        choice_1 = choices[0]  # assigning each dictionary to a list index
        choice_2 = choices[1]
        if choice_1 != choice_2:
            no_repeat = False
        elif choice_1 == choice_2:
            no_repeat = True


def higher_or_lower():
    prompt = input(f"\n########################### \n    Higher or lower? \n\nWho: {choice_1['name']}, "
                   f"What: {choice_1['description']}, "
                   f"Where: {choice_1['country']}\n \n         OR \n"
                   f"\n{choice_2['name']}, {choice_2['description']}, {choice_2['country']}?"
                   f"\n\nEnter 'higher' if {choice_1['name']} has more followers than "
                   f"{choice_2['name']}, "
                   f"or 'lower' for vice-versa.\n##########################\n").lower()

    follower_count_1 = choice_1["follower_count"]  # assigning variables for values from follower count key
    follower_count_2 = choice_2["follower_count"]
    compare = follower_count_1 > follower_count_2  # comparing values, compare default set to greater than
    print(f"Followers: {follower_count_1}, {follower_count_2}")
    if compare is True and prompt == 'higher':  # if true and prompt also higher, correct, return true
        print("Correct!")                       # tethering higher string to comparison
        return True
    elif compare is False and prompt == 'lower':  # if false and prompt also false, correct, return true
        print("Correct!")
        return True
    else:
        print("Incorrect")
        return False






print("Captain William Presents: ")
print(logo)
game = True
score = 0
while game is True:
    call_followers()
    gameplay = higher_or_lower()  # function must be set to a variable to be able to have returns work
    if gameplay is True:
        score += 1
        print(f"score: {score}")
    else:
        print(f"final score: {score}")
        score = 0
        replay = input("Play again? y/n: ")
        if replay == 'y':
            game = True
            print(logo)
        else:
            game = False
            print("Thanks for playing!")
            exit()
