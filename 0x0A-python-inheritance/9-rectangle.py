#!/usr/bin/python3
""" rectangle module """
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """ rectangle inherits from BaseGeometry """

    def __init__(self, width, height):
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__height = height
        self.__width = width

    def area(self):
        """ area of rectangle """
        return self.__height * self.__width

    def __str__(self):
        return "[Rectangle] {}/{}".format(self.__width, self.__height)
