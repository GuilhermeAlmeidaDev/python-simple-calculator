# calculator/app/operations/root.py

# Description: Square root operation
def square_root(x: float) -> float:
    """
    Calculate the square root of a number.

    Args:
        x (float): The number.

    Returns:
        float: The square root of the number.

    Raises:
        TypeError: If the argument is not a number.
        ValueError: If the number is negative.
    """

    try:
        # Check if the argument is negative
        if x < 0:
            raise ValueError("Cannot compute square root of a negative number")

        # Check if the argument is a number
        if isinstance(x, (int, float)):
            return x ** 0.5
        
        else:
            raise TypeError("Arguments must be numbers")
        
    except ValueError as e:
        return f"ValueError: {e}"

    except ZeroDivisionError as e:
        return f"Error: {e}"
    
    except TypeError as e:
        return f"Error: {e}"
    
    
if __name__ == "__main__":
    print(square_root(16))    # Output: 4.0
    print(square_root(25))    # Output: 5.0
    print(square_root(144))   # Output: 12.0
    print(square_root(-1))    # Output: ValueError: Cannot compute square root of a negative number
    print(square_root('16'))  # Output: Error: Arguments must be numbers
    print(square_root(0))     # Output: 0.0