#!/usr/bin/python3
""" my module """


def write_file(filename="", text=""):
    """ Write a file """
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(text)
        return len(text)
