# calculator/app/operations/division.py

# Description: division operation
def divide(*args: int) -> int:
    """
    Perform division on multiple numbers.

    Args:
        *args: Numbers to be divided.

    Returns:
        int: The division of the numbers.

    Raises:
        ZeroDivisionError: If the divisor is zero.
        TypeError: If any argument is not a number.
    """

    try:
        # Check if all arguments are integers
        if all(isinstance(arg, (int, float)) for arg in args):
            return args[0] / sum(args[1:])
        else:
            raise TypeError("Arguments must be numbers")
        
    except ZeroDivisionError as e:
        return f"Error: {e}"
        
    except TypeError as e:
        return f"Error: {e}"


if __name__ == "__main__":
    print(divide(10, 0))    # Output: Error: division by zero
    print(divide(2, 4))     # Output: 0.5
    print(divide(1, '2'))   # Output: Error: Arguments must be numbers
    print(divide('1', '2')) # Output: Error: Arguments must be numbers
    print(divide(1, 'a'))   # Output: Error: Arguments must be numbers
    print(divide(3, 2.0))   # Output: 1.5
    print(divide(1, 2, 3))  # Output: 0.2
    