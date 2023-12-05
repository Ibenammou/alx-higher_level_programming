#!/usr/bin/python3
"""Class Student"""


class Student:

    def __init__(self, first_name, last_name, age):
        """Constructor
            Args:
                first_name
                last_name
                age
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        Public instance attribute
        """
        if (isinstance(attrs, list) and
                all(isinstance(x, str) for x in attrs)):
            return {x: getattr(self, x) for x in attrs if hasattr(self, x)}
        return self.__dict__
