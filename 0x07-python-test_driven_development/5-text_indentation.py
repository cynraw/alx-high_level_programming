#!/usr/bin/python3
"""text indent, task 5 in python test driven development"""


def text_indentation(text):
    """function that indents text 
    Args:
        text- string
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    for delimeter in "?:.":
        words = (delimeter + "\n\n").join(
                [index.strip(" ") for index in words.split(delimeter)])


if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/5-text_indentation.txt")
