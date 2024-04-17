# Description: Subtraction operation
def subtract(*args: int) -> int:
    try:
        # Check if all arguments are integers
        if all(isinstance(arg, (int, float)) for arg in args):
            return args[0] - sum(args[1:])
        else:
            return "Arguments must be numbers"
    except:
        return "An unexpected error occurred"

 
if __name__ == "__main__":
    print(subtract(1, 2))
    print(subtract(1, '2'))
    print(subtract('1', '2'))
    print(subtract(1, 'a'))
    print(subtract(1, 2.0))
    print(subtract(1, 2, 3))