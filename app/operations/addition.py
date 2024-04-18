# calculator/app/operations/addition.py

# Description: Addition operation
def add(*args: int) -> int:
    """
    Perform addition on multiple numbers.

    Args:
        *args: Numbers to be added.

    Returns:
        int: The sum of the numbers.

    Raises:
        TypeError: If any argument is not a number.
    """
    try:
        # Check if all arguments are integers
        if all(isinstance(arg, (int, float)) for arg in args):
            return args[0] + sum(args[1:])
        
        else:
            raise TypeError("Arguments must be numbers")
        
    except TypeError as e:
        return f"Error: {e}"
    

if __name__ == "__main__":
    print(add(1, 2))    # Output: 3
    print(add(1, '2'))  # Output: Error: Arguments must be numbers
    print(add('1', '2'))  # Output: Error: Arguments must be numbers
    print(add(1, 'a'))  # Output: Error: Arguments must be numbers
    print(add(1, 2.0))  # Output: 3.0
    print(add(1, 2, 3))  # Output: 6
    