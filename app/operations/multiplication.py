# Description: Multiplication operation
def multiply(*args: int) -> int:
    try:
        # Check if all arguments are integers
        if all(isinstance(arg, (int, float)) for arg in args):
            return args[0] * sum(args[1:])
        else:
            return "Arguments must be numbers"
    except:
        return "An unexpected error occurred"


if __name__ == "__main__":
    print(multiply(2, 4))
    print(multiply(1, '2'))
    print(multiply('1', '2'))
    print(multiply(1, 'a'))
    print(multiply(3, 2.0))
    print(multiply(1, 2, 3))
    