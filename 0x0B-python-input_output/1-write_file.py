#!/usr/bin/python3
"""
Module for writing to a file
"""


def write_file(filename="", text=""):
    """
    Writes a string to a text file (UTF8) and returns the number of characters written.

    Args:
        filename (str): The name of the file.
        text (str): The text to write to the file.

    Returns:
        int: The number of characters written.
    """
    with open(filename, mode='w', encoding='utf-8') as file:
        return file.write(text)


if __name__ == "__main__":
    filename = "my_first_file.txt"
    text = "This School is so cool!\n"
    nb_characters = write_file(filename, text)
    print(nb_characters)

