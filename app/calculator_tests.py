# Importing area
from os import system
from operations.addition import add
from operations.subtraction import subtract
from operations.multiplication import multiply
from operations.division import divide
from operations.percent import percent
from operations.root import square_root


class Calculator:
    def __init__(self):
        
        # Dictionary to store the operations
        self.operations = {
            "+": add,
            "-": subtract,
            "*": multiply,
            "/": divide,
            "%": percent,
            "root": square_root
        }


    def calculation(self, num1: float, operator: str, num2: float) -> float:
        try:
            if isinstance(num1, (int, float)) and isinstance(num2, (int, float)):
                pass
            
            else:
                raise TypeError("Arguments must be numbers")
            
            if operator not in self.operations:
                print("Invalid operator")

            elif operator == "root":
                return self.operations[operator](num1)


            # Return the user input if everything is valid
            return self.operations[operator](num1, num2)

        # Check value is a number
        except ValueError as e:
            return f"Error: {e}"

        except ZeroDivisionError as e:
            return f"Error: {e}"
    
        except TypeError as e:
            return f"Error: {e}"


if __name__ == "__main__":
    system("cls")
    calculator = Calculator()
    num1 = float(input("Enter the first number: "))
    operator = input("Enter the operation (+, -, *, /, %, root): ")

    if operator == "root":
        result = calculator.calculation(num1, operator, 0)

        if result == int(result):
            print(f"Result: {int(result)}")

        else:
            print(f"Result: {result}")

        exit()

    num2 = float(input("Enter the second number: "))
    result = calculator.calculation(num1, operator, num2)
    if result == int(result):
        print(f"Result: {int(result)}")
    else:
        print(f"Result: {result}")

