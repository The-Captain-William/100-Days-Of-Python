import random


def draw_card(cards):
    index_draw = random.choice(range(len(cards)))  # in the range of the number of cards
    card_draw = cards[index_draw]  # card is cards[card index]; object is equal to object in card list, index number
    cards.pop(index_draw)  # remove card from deck
    return card_draw  # draw card




