#!/usr/bin/python3
"""Defines a square"""


class Square:
    """Define a square class"""

    def __init__(self, size=0):
        """class definition
        Args:
            size: instance of attribute
        """
        self.size = size

    @property
    def size(self):
        """Define the size"""
        return self._size

    @size.setter
    def size(self, value):
        """Define the size setter
        Args:
            value: value param
        """
        if not isinstance(value, (float, int)):
            raise TypeError("size must be a number")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self._size = value

    def area(self):
        """Define area"""
        return self.size ** 2

    def __eq__(self, other):
        """Define the equall == operator"""
        if isinstance(other, Square):
            return self.area() == other.area()
        return False

    def __ne__(self, other):
        """Define not equall != operator"""
        return not self.__eq__(other)

    def __gt__(self, other):
        """Define greater > operator"""
        if isinstance(other, Square):
            return self.area() > other.area()
        return False

    def __ge__(self, other):
        """Define greater than or equall >= operator"""
        if isinstance(other, Square):
            return self.area() >= other.area()
        return False

    def __lt__(self, other):
        """Defines less than < operator"""
        if isinstance(other, Square):
            return self.area() < other.area()
        return False

    def __le__(self, other):
        """Defines less than or equall <= operator"""
        if isinstance(other, Square):
            return self.area() <= other.area()
        return False
