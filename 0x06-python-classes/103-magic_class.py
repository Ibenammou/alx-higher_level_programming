#!/usr/bin/python3
"""This module defines the MagicClass."""

import math

class MagicClass:
    """This class represents a MagicClass with radius-related operations."""

    def __init__(self, radius=0):
        """
        Initialize the MagicClass instance with a radius.

        Args:
            radius (int or float): The radius of the MagicClass.
        """
        self.__radius = 0  # Double underscore to emulate name mangling
        self.radius = radius

    @property
    def radius(self):
        """Get the radius of the MagicClass."""
        return self.__radius

    @radius.setter
    def radius(self, value):
        """
        Set the radius of the MagicClass.

        Args:
            value (int or float): The new radius value.
        """
        if not isinstance(value, (int, float)):
            raise TypeError("radius must be a number")
        self.__radius = value

    def area(self):
        """Calculate and return the area of the MagicClass."""
        return self.__radius ** 2 * math.pi

    def circumference(self):
        """Calculate and return the circumference of the MagicClass."""
        return 2 * math.pi * self.__radius

