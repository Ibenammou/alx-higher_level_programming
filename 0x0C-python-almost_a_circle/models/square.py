#!/usr/bin/python3
""" Square Module """
from models.rectangle import Rectangle

class Square(Rectangle):
    """ Square class, inherits from Rectangle """

    def __init__(self, size, x=0, y=0, id=None):
        """ Constructor method """
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """ Override __str__ method to represent Square object as a string """
        return "[Square] ({}) {}/{} - {}".format(
            self.id, self.x, self.y, self.width
        )

if __name__ == "__main__":
    # Example usage
    s1 = Square(5)
    print(s1)
    print(s1.area())
    s1.display()

    print("---")

    s2 = Square(2, 2)
    print(s2)
    print(s2.area())
    s2.display()

    print("---")

    s3 = Square(3, 1, 3)
    print(s3)
    print(s3.area())
    s3.display()

