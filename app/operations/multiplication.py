# calculator/app/operations/multiplication.py

# Description: Multiplication operation
def multiply(*args: int) -> int:
    """
    Perform multiplication on multiple numbers.

    Args:
        *args: Numbers to be multiplied.

    Returns:
        int: The product of the numbers.

    Raises:
        TypeError: If any argument is not a number.
    """

    try:
        # Check if all arguments are integers
        if all(isinstance(arg, (int, float)) for arg in args):
            return args[0] * sum(args[1:])
        
        else:
            raise TypeError("Arguments must be numbers")
        
    except TypeError as e:
        return f"Error: {e}"


if __name__ == "__main__":
    print(multiply(2, 4))
    print(multiply(1, '2'))
    print(multiply('1', '2'))
    print(multiply(1, 'a'))
    print(multiply(3, 2.0))
    print(multiply(1, 2, 3))
    