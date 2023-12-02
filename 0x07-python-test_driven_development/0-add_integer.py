#!/usr/bin/python3
"""
add_integer:
This is the "0-add_integer" module.
my function add_integer(a, b)
"""


def add_integer(a, b=98):
    """
    Description:
            return an integer: addition of a and b
    Parameters:
            a (int or float): an integer.
            b (int or float): an integer default is 98.

    Returns:
            int: addition of a and b.

    Raises:
            TypeError: If a or b is not an integer or float
    """
    if type(a) is not int and type(a) is not float:
        raise TypeError("a must be an integer")
    if type(b) is not int and type(b) is not float:
        raise TypeError("b must be an integer")
    if type(a) is float:
        a = int(a)
    if type(b) is float:
        b = int(b)
    return a + b
