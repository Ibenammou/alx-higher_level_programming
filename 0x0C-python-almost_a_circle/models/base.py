# models/rectangle.py

#!/usr/bin/python3
"""
Module for Rectangle class.
"""

from models.base import Base

class Rectangle(Base):
    """
    The Rectangle class.
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """
        Initializes a new instance of Rectangle.

        Args:
            width (int): The width of the rectangle.
            height (int): The height of the rectangle.
            x (int): The x-coordinate of the rectangle.
            y (int): The y-coordinate of the rectangle.
            id (int): The identifier.

        Returns:
            None.
        """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @staticmethod
    def save_to_file(list_objs):
        """
        Writes the JSON string representation of a list of instances to a file.

        Args:
            list_objs (list): A list of instances.

        Returns:
            None.
        """
        filename = "{}.json".format(type(list_objs[0]).__name__)
        json_list = []
        if list_objs is not None:
            for obj in list_objs:
                json_list.append(obj.to_dictionary())
        with open(filename, mode="w", encoding="utf-8") as file:
            file.write(Base.to_json_string(json_list))

