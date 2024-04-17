# Importing area
from operations.addition import add
from operations.subtraction import subtract
from operations.multiplication import multiply
from operations.division import divide

# Dictionary to store the operations
operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}

def user_input():
    while True:
        try:
            # Get the user input for the first number
            num1 = float(input("Enter the first number: "))

            # Get the user input for the operator
            operator = input("Enter the operation (+, -, *, /): ")

            # Check if the operator is valid
            if operator not in operations:
                print("Invalid operator")
                continue

            # Get the user input for the second number
            num2 = float(input("Enter the second number: "))

            # Return the user input if everything is valid
            return operations[operator](num1, num2)

        # Check value is a number
        except ValueError:
            print("Please enter a valid number")
            continue

def main():
    result = user_input()
    if result == int(result):
        return print(f"Result: {int(result)}")
    else:
        return print(f"Result: {result}")
    

if __name__ == "__main__":
    main()

