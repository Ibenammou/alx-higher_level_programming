#!/usr/bin/python3
"""Defines a square"""


class Square:
    """Square defines the class square

    Attribute:
        Square class
    """
    def __init__(self, size=0):
        """Create the instance of a square

        Args:
            size: private instance attribute
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def area(self):
        return self.__size ** 2
