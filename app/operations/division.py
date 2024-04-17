# Description: division operation
def divide(*args: int) -> int:
    try:
        # Check if all arguments are integers
        if all(isinstance(arg, (int, float)) for arg in args):
            return args[0] / sum(args[1:])
        else:
            return "Arguments must be numbers"
    
    except ZeroDivisionError:
        return "Division by zero is not allowed"
    
    except:
        return "An unexpected error occurred"


if __name__ == "__main__":
    print(divide(10, 0))
    print(divide(2, 4))
    print(divide(1, '2'))
    print(divide('1', '2'))
    print(divide(1, 'a'))
    print(divide(3, 2.0))
    print(divide(1, 2, 3))
    