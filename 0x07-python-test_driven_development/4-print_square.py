#!/usr/bin/python3
"""4-print_square, created for task 4 of python test driven development.
"""

def print_square(size):
    """print_square, a funtion that prints a square out of the argument size.
    Args:
    size- integer (size of the square)
    """
    if isinstance not (size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    for index in range(size):
        print("x" * size)
