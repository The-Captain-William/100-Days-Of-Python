import random
from logo import logo
from draw_card import draw_card
fresh_game = True

print(logo)
print("Captain William Presents: Blackjack")

while fresh_game is True:  # random cards drawn

    loop_cards = True
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]  # custom deck
    computer_total = 0
    player_total = 0

    players_cards = []
    computers_cards = []
    for deals in range(2):  # 0, 1
        players_cards.append(draw_card(cards))
        computers_cards.append(draw_card(cards))
    fresh_game = False

    computers_hand = computers_cards[random.randint(0, 1)]

    while loop_cards is True:  # nested in fresh_game and will run because fresh game was true once
        print(cards)
        player_total = sum(players_cards)
        computer_total = sum(computers_cards)
        print(f"\nDealers Cards: [{computers_hand}, #]")  # hidden card
        print(f"Players Cards: {players_cards} sum:{player_total}")

        hit_or_hold = input("\nHit, or hold? y to hit, n to hold: ").lower()
        if hit_or_hold == 'y':  # will loop cards shown to make code cleaner
            players_cards.append(draw_card(cards))
            player_total = sum(players_cards)
            if player_total > 21:
                print("\nBust! You lose!")
                print(f"Dealers Cards: {computers_cards} sum: {computer_total}")
                print(f"Players Cards: {players_cards} sum:{player_total}")
                loop_cards = False
            elif player_total <= 21:
                pass
        elif hit_or_hold == 'n':
            loop_cards = False  # above terminates and below initiates
        else:
            print("Invalid key")
            pass

    while loop_cards is False:  # note these while loops are in the same indent
        if player_total <= 21:
            print("\nRevealing House Cards:")
            print(f"\nDealers Cards: {computers_cards} sum:{computer_total}")
            print(f"Players Cards: {players_cards} sum:{player_total}")

            player_total = sum(players_cards)
            computer_total = sum(computers_cards)

            if computer_total < 16:
                computers_cards.append(draw_card(cards))
                computer_total = sum(computers_cards)
                print("\nDealer drawing New Card...")
                print(f"\nDealers Cards: {computers_cards} sum: {computer_total}")
                print(f"Players Cards: {players_cards} sum:{player_total}")

                if computer_total > 21:
                    print("\nHouse busts! You win!")

            if player_total > computer_total:
                print("\nPlayer wins!")
            elif player_total == computer_total:
                print("\nDraw!")
            elif player_total < computer_total:
                print("\nHouse wins!")
        loop_cards = True  # will terminate above action

    play_again = input("\nPlay again? y/n: ").lower()  # already initiated because fresh_game was once true

    if play_again == "y":
        fresh_game = True
    elif play_again == "n":
        print("\nThanks for playing!")
        exit()
    else:
        pass
