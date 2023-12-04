#!/usr/bin/python3
""" basegeometry module """


class BaseGeometry:
    """my basegetmetry class"""
    pass

    def area(self):
        """
        Area
        Exception
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        validation
        name : string
        """
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
