import art
def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
}

def calculator():
    print(art.logo)
    n1 = float(input("What's the first number?\n"))
    should_accumulate = True

    while should_accumulate:
        for key in operations:
            print(key)

        chosen_operation = input("Pick an operation:")
        n2 = float(input("What's the next number?"))

        result = operations[chosen_operation](n1, n2)
        print(f"{n1} {chosen_operation} {n2} = {operations[chosen_operation](n1, n2)}")

        continue_with_result = input(f"Type 'y' to continue calculating with {result}, or type 'n' to start a new calculation:").lower()
        if continue_with_result == "y":
            n1 = result
        else:
            should_accumulate = False
            print("\n" * 20)
            calculator()

calculator()








