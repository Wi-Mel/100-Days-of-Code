import art
print(art.logo)
continue_bidding = True
auction = {}

while continue_bidding:

    bidder_name = input("What is your name?\n")
    bid = int(input("What is your bid? $"))
    auction[bidder_name] = bid

    bidders_quest = input("Type 'yes' if there are more players or 'no' if there are no more players\n").lower()

    if bidders_quest == "yes":
        print("\n" * 100)

    else:
        continue_bidding = False
        max_key = max(auction, key = auction.get)
        print(f"The winner is {max_key} with a bid of ${auction[max_key]}")
