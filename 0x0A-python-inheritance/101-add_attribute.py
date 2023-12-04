#!/usr/bin/python3
"""Defines and add a new attribute to an object"""


def add_attribute(obj, attr_name, attr_value):
    """Define add_attribute
    Args:
        obj
        attr_name
        attr_value
    """
    if not hasattr(obj, '__dict__'):
        raise TypeError("can't add new attribute")
    setattr(obj, attr_name, attr_value)
