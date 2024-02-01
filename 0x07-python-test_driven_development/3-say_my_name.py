#!/usr/bin/python3
"""3-say_my_name, created for task 2 of python test driven development.
"""

def say_my_name(first_name, last_name=""):
    """say_my_name, a function that prints the name of the person passed.
    Args:
    first_name- string 
    last_name- string
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    print("My name is {:s} {:s}".format(first_name, last_name))
