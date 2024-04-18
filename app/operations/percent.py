# calculator/app/operations/percent.py

# Description: percentage operation
def percent(x: float, y: float) -> float:
    """
    Calculate the percentage of a number.

    Args:
        x (float): The number.
        y (float): The percentage.

    Returns:
        float: The result of the percentage calculation.
    """

    try:
        return (x * y) / 100
    
    except TypeError:
        return "Error: Arguments must be numbers"
    
    except ZeroDivisionError:
        return "Error: Cannot divide by zero"


if __name__ == "__main__":
    print(percent(50, 10))    # Output: 5.0
    print(percent(100, 20))   # Output: 20.0
    print(percent(200, 25))   # Output: 50.0
    print(percent(50, '10'))  # Output: Error: Arguments must be numbers
    print(percent(50, 0))     # Output: Error: Cannot divide by zero
