# calculator/cli_calculator.py

# Importing area
from os import system
from app.operations import add, subtract, multiply, divide, percent, square_root

# Dictionary to store the operations
operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
    "%": percent,
    "root": square_root
}


def user_input_cli():
    while True:
        try:
            # Get the user input for the first number
            num1 = float(input("Enter the first number: "))

            # Get the user input for the operator
            operator = input("Enter the operation (+, -, *, /, %, root): ")

            # Check if the operator is valid
            if operator not in operations:
                print("Invalid operator")
                continue
            elif operator == "root":
                return operations[operator](num1)

            # Get the user input for the second number
            num2 = float(input("Enter the second number: "))

            # Return the user input if everything is valid
            return operations[operator](num1, num2)

        # Check value is a number
        except ValueError:
            print("Please enter a valid number")
            continue

def main():
    result = user_input_cli()
    if result == int(result):
        return print(f"Result: {int(result)}")
    else:
        return print(f"Result: {result}")
    

if __name__ == "__main__":
    system("cls")
    main()

