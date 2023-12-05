#!/usr/bin/python3
"""
my mmodule
"""


def read_file(filename=""):
    """ the function read_file  """
    with open(filename, 'r', encoding="utf-8") as f:
        read = f.read()
        print(read, end="")
