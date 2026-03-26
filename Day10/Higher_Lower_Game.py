import random
from game_data import data
import art

random.shuffle(data)

score = 0
game_on = True
while game_on:
    print(art.logo)
    for i in range(len(data) - 1):
        print(f"Compare A: {data[i]['name']}, {data[i]['description']}, {data[i]['country']}")
        print(art.vs)
        print(f"Against B: {data[i + 1]['name']}, {data[i + 1]['description']}, {data[i + 1]['country']}")

        followers = {
            "A": data[i]['follower_count'],
            "B": data[i + 1]['follower_count'],
        }

        answer = input("Who has more followers? Type 'A' or 'B':").upper()
        print("\n" * 100)
        print(art.logo)

        if answer == "A" and followers["A"] > followers["B"]:
            score += 1
            print(f"You're right! Current score: {score}")
        elif answer == "B" and followers["B"] > followers["A"]:
            score += 1
            print(f"You're right! Current score: {score}")
        else:
            game_on = False
            print(f"Sorry, that's wrong. Final score: {score}")
            break
