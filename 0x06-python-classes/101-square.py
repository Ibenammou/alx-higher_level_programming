#!/usr/bin/python3
"""Defines a square by: (based on 6-square.py)"""


class Square:
    """Defines a square by: (based on 6-square.py)
    """

    def __init__(self, size=0, position=(0, 0)):
        """Defines a square class

        Args:
            size: attribute size
            position: attribute space position
        """
        self.size = size
        self.position = position

    @property
    def size(self):
        """Define the size"""
        return self._size

    @size.setter
    def size(self, value):
        """Define the size setter
        Args:
            value: property value
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self._size = value

    @property
    def position(self):
        """Define the position"""
        return self._position

    @position.setter
    def position(self, value):
        """Define the position setter
        Args:
            value: property value
        """
        if (
            not isinstance(value, tuple) or
            len(value) != 2 or
            not all(isinstance(i, int) for i in value) or
            not all(i >= 0 for i in value)
        ):
            raise TypeError("position must be a tuple of 2 positive integer")
        self._position = value

    def area(self):
        """Define the area"""
        return self.size ** 2

    def __str__(self):
        """Define the str method"""
        if self.size == 0:
            return ""
        else:
            result = ""
        for _ in range(self.position[1]):
            result += "\n"
        for _ in range(self.size):
            result += " " * self.position[0] + "#" * self.size + "\n"
        return result.rstrip()
