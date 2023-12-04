#!/usr/bin/python3
"""
check : inherited
"""


def inherits_from(obj, a_class):
    """
    check : inherited
    """
    return issubclass(type(obj), a_class) and type(obj) is not a_class
