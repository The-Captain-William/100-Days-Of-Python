logo = '''
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\\
                       .-------------.
                      /_______________\\
'''


print(logo, "\n Blind Auction Simulator")
other_bidders = True
next_stage = False
auction = {}


def find_highest_bidder(auction_record):
    highest_bid = 0
    winner = ""
    for bidder in auction_record:  # for loops will loop through keys
        bid_amount = auction_record[bidder]  # "auction record" == a given dictionary.
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder
    print(f"The winner is {winner} with a bid of ${highest_bid}")


while other_bidders is True:
    # opening screen
    next_stage = True
    name = input("What's your name?: ")
    bid = int(input("What's your bid?: "))
    auction[name] = bid
    while next_stage is True:
        bidders = input("Are there other bidders? y/n: ").lower()
        if bidders == "y":
            other_bidders = True
            next_stage = False
        elif bidders == "n":
            other_bidders = False
            next_stage = False
        else:
            print("Incorrect Answer")
            other_bidders = False

find_highest_bidder(auction)
