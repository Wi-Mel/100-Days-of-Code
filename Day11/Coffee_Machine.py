MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

def check_resources(prompt):
    for ingredient in MENU[prompt]["ingredients"]:
        if MENU[prompt]["ingredients"][ingredient] > resources[ingredient]:
            print(f"Sorry there is not enough {ingredient}.")
            return False
    return True

def check_transaction(coins_value):
    if coins_value < MENU[prompt]["cost"]:
        print("Sorry that's not enough money. Money refunded.")
        return False
    elif coins_value >= MENU[prompt]["cost"]:
        global money
        money += MENU[prompt]["cost"]
        for ingredient in MENU[prompt]["ingredients"]:
            resources[ingredient] -= MENU[prompt]["ingredients"][ingredient]

        if coins_value > MENU[prompt]["cost"]:
            change = round((coins_value - MENU[prompt]["cost"]), 2)
            print(f"Here is ${change} in change.")

        print(f"Here is your {prompt}☕. Enjoy!")

        return True

money = 0

machine_on = True
while machine_on:
    prompt = input("What would you like? (espresso/ latte/ cappuccino): ").lower()
    if prompt == "off":
        quit()
    elif prompt == "report":
        print(f"Water: {resources["water"]}ml\nMilk: {resources["milk"]}ml\nCoffee: {resources["coffee"]}g\nMoney: ${money}\n")
    elif prompt in MENU:
        sufficient = check_resources(prompt)
        if sufficient:
            print("Please insert coins.")
            quarters = int(input("how many quarters? "))
            dimes = int(input("how many dimes? "))
            nickles = int(input("how many nickles? "))
            pennies = int(input("how many pennies? "))
            coins_value = (0.25 * quarters) + (0.10 * dimes) + (0.05 * nickles) + (0.01 * pennies)

            check_transaction(coins_value)

