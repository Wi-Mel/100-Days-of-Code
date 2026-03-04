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
symbols = [rock, paper, scissors]

user_choice = int(input("Welcome to the Game: Rock, Paper, Scissors!\nWhat do you choose?\nTpe 0 for Rock, 1 for Paper, or 2 for Scissors"))
if user_choice in range(0,3):
    if user_choice == 0:
        print(f"You have chosen:\n{symbols[0]}")
    elif user_choice == 1:
        print(f"You have chosen:\n{symbols[1]}")
    elif user_choice == 2:
        print(f"You have chosen:\n{symbols[2]}")


    comp_choice = random.randint(0, 2)
    if comp_choice == 0:
        print(f"Computer chose:\n{symbols[0]}")
    if comp_choice == 1:
        print(f"Computer chose:\n{symbols[1]}")
    if comp_choice == 2:
        print(f"Computer chose:\n{symbols[2]}")

    if comp_choice == 2 and user_choice == 0:
        print("You Win!")
    elif comp_choice == 0 and user_choice == 2:
        print("You Lose!")
    elif user_choice > comp_choice:
        print("You Win!")
    elif user_choice == comp_choice:
        print("It's a draw!")
    else:
        print("You Lose!")

else:
    print("Your input is invalid. You lose!")
