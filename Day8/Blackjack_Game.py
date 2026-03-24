import random
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

def play_blackjack():
    return input("Do you want to play a game of Blackjack? Type 'y' or 'n':").lower()

choose_to_play = play_blackjack()
while choose_to_play == "y":
    player_cards = random.sample(cards, 2)

    dealer_cards = random.sample(cards, 2)

    player_sum = sum(player_cards)
    dealer_sum = sum(dealer_cards)
    print(f"Your cards: {player_cards}, current score: {player_sum}\nDealer's first card: {dealer_cards[0]}")

    game_over = False
    while not game_over:
        player_choice = input("Type 'y' to pick another card, or 'n' to pass:").lower()

        if player_choice == "n":
            if player_sum == 21:
                game_over = True
                print(f"Dealer's final hand: {dealer_cards}, final score:{dealer_sum}\nYour final hand:{player_cards}, final score:{player_sum}")
                print("Blackjack♦️♣️♥️♠️! You the player wins😁!")
            elif dealer_sum == 21:
                game_over = True
                print(f"Dealer's final hand: {dealer_cards}, final score:{dealer_sum}\nYour final hand:{player_cards}, final score:{player_sum}")
                print("Blackjack♦️♣️♥️♠️! You the player have lost to the house😥!")
            elif dealer_sum >= 17:
                if dealer_sum > player_sum:
                    game_over = True
                    print(f"Dealer's final hand: {dealer_cards}, final score:{dealer_sum}\nYour final hand:{player_cards}, final score:{player_sum}")
                    print("You the player have lost to the house😥!")
                else:
                    game_over = True
                    print(f"Dealer's final hand: {dealer_cards}, final score:{dealer_sum}\nYour final hand:{player_cards}, final score:{player_sum}")
                    print("You the player wins😁!")
            elif dealer_sum < 17:
                dealer_cards.append(random.choice(cards))
                dealer_sum += dealer_cards[len(dealer_cards) - 1]

                while dealer_sum <17:
                    dealer_cards.append(random.choice(cards))
                    dealer_sum += dealer_cards[len(dealer_cards) - 1]

                if dealer_sum == 21:
                    game_over = True
                    print(f"Dealer's final hand: {dealer_cards}, final score:{dealer_sum}\nYour final hand:{player_cards}, final score:{player_sum}")
                    print("Blackjack♦️♣️♥️♠️! You the player have lost to the house😥!")
                elif dealer_sum > 21:
                    game_over = True
                    print(f"Dealer's final hand: {dealer_cards}, final score:{dealer_sum}\nYour final hand:{player_cards}, final score:{player_sum}")
                    print("You the player wins😁!")
                elif dealer_sum > player_sum:
                    game_over = True
                    print(f"Dealer's final hand: {dealer_cards}, final score:{dealer_sum}\nYour final hand:{player_cards}, final score:{player_sum}")
                    print("You the player have lost to the house😥!")
                elif player_sum > dealer_sum:
                    game_over = True
                    print(f"Dealer's final hand: {dealer_cards}, final score:{dealer_sum}\nYour final hand:{player_cards}, final score:{player_sum}")
                    print("You the player wins😁!")

        elif player_choice == "y":
            player_cards.append(random.choice(cards))
            player_sum += player_cards[len(player_cards) - 1]

            if player_sum > 21 and 11 in player_cards:
                player_cards[player_cards.index(11)] = 1
                player_sum = sum(player_cards)
                print(f"Your cards: {player_cards}, current score: {player_sum}\nDealer's first card: {dealer_cards[0]}")
            elif player_sum > 21:
                game_over = True
                print(f"Dealer's final hand: {dealer_cards}, final score:{dealer_sum}\nYour final hand:{player_cards}, final score:{player_sum}")
                print(f"You the player has exceeded 21.You lose😥!")
            else:

                print(f"Your cards: {player_cards}, current score: {player_sum}\nDealer's first card: {dealer_cards[0]}")



    play_blackjack()


