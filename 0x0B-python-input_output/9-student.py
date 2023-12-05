#!/usr/bin/python3
"""Define class student"""


class Student:
    """Class Student"""

    def __init__(self, first_name, last_name, age):
        """public instanc attr
        Args:
            first_name
            last_name
            age
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """ Class Dictionary
        """
        return self.__dict__.copy()
