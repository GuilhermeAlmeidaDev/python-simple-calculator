# calculator/app/operations/subtraction.py

# Description: Subtraction operation
def subtract(*args: int) -> int:
    """
    Perform subtraction on multiple numbers.

    Args:
        *args: Numbers to be subtracted.

    Returns:
        int: The difference of the numbers.

    Raises:
        TypeError: If any argument is not a number.
    """

    try:
        # Check if all arguments are integers
        if all(isinstance(arg, (int, float)) for arg in args):
            return args[0] - sum(args[1:])
        
        else:
            raise TypeError("Arguments must be numbers")
        
    except TypeError as e:
        return f"Error: {e}"

 
if __name__ == "__main__":
    print(subtract(1, 2))
    print(subtract(1, '2'))
    print(subtract('1', '2'))
    print(subtract(1, 'a'))
    print(subtract(1, 2.0))
    print(subtract(1, 2, 3))