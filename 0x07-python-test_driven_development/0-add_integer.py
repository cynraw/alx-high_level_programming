#!/usr/bin/python3

"""
This module contains the add_integer function

"""

def add_integer(a, b):
    """
    This function adds two numbers integer or float

    Args:
        a (int/float): The first number
        b (int/float): The second number

    Returns:
        int: The sum of a and b
    """
  
    if not isinstance(a, int) and not isinstance(a, float):
        raise TypeError("a must be an integer or a float")

    if not isinstance(b, int) and not isinstance(b, float):
        raise TypeError("b must be an integer or a float")

    a = int(a)
    b = int(b)

    return(a + b)
