import random
import art
print(art.logo)
right_integer = random.randint(1,100)

print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")
difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()

attempts_by_difficulty = {
    "easy": 10,
    "hard": 5,
}

def ten_or_five_attempts():
        print(f"You have {attempts_by_difficulty[difficulty]} attempts remaining to guess the number.")
        guess = int(input("Make a guess: "))
        if guess == right_integer:
            global continue_guessing
            continue_guessing = False
            print(f"You got it😎! The answer was {right_integer}.")

        elif guess != right_integer:
            attempts_by_difficulty[difficulty] -= 1
            if attempts_by_difficulty[difficulty] == 0:
                continue_guessing = False
                print("You've run out of guesses😥.")
            else:
                if guess < right_integer:
                    print("Too Low.\nGuess again.")
                else:
                    print("Too High.\nGuess again.")

continue_guessing = True
while continue_guessing:
    ten_or_five_attempts()








