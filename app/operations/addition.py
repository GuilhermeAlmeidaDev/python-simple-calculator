# Description: Addition operation
def add(*args: int) -> int:
    try:
        # Check if all arguments are integers
        if all(isinstance(arg, (int, float)) for arg in args):
            return args[0] + sum(args[1:])
        else:
            return "Arguments must be numbers"
    except:
        return "An unexpected error occurred"
    

if __name__ == "__main__":
    print(add(1, 2))
    print(add(1, '2'))
    print(add('1', '2'))
    print(add(1, 'a'))
    print(add(1, 2.0))
    print(add(1, 2, 3))
    