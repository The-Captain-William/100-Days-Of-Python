# rock paper scissors
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
# rock beats scissors
# scissors beats paper
# paper beats rock

choices = [rock, paper, scissors]
print("Welcome To Rock Paper Scissors!")
repeat = True


while repeat is True:
    player = input("Rock, paper, or Scissors? (Type anything else to stop): ")
    computer_choice = random.choice(choices)
    player_choice = []
    print("Player:")
    if player.lower() == "rock":
        player_choice.append(rock)
        print(rock)
    elif player.lower() == "paper":
        player_choice.append(paper)
        print(paper)
    elif player.lower() == "scissors":
        player_choice.append(scissors)
        print(scissors)
    else:
        print("Thanks for playing!")
        break



    print("Computer:")
    if computer_choice == rock:
        print(rock)
    elif computer_choice == paper:
        print(paper)
    elif computer_choice == scissors:
        print(scissors)
    else:
        pass

    computer_w = "Computer wins!"
    player_w = "Player wins!"

    if computer_choice == player_choice[0]:  # draw
        print("Draw!")
    elif player_choice[0] == rock and computer_choice == paper:
        print(computer_w)
    elif player_choice[0] == rock and computer_choice == scissors:
        print(player_w)
    elif player_choice[0] == paper and computer_choice == rock:
        print(player_w)
    elif player_choice[0] == paper and computer_choice == scissors:
        print(computer_w)
    elif player_choice[0] == scissors and computer_choice == rock:
        print(computer_w)
    elif player_choice[0] == scissors and computer_choice == paper:
        print(player_w)



