#!/usr/bin/python3
""" Base Module """
class Base:
    """ Base class for managing id attribute """

    # Private class attribute
    __nb_objects = 0

    def __init__(self, id=None):
        """ Constructor method """
        if id is not None:
            # If id is provided, assign it to the public instance attribute
            self.id = id
        else:
            # Increment __nb_objects and assign the new value to the public instance attribute id
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

if __name__ == "__main__":
    # Example usage
    b1 = Base()
    print(b1.id)

    b2 = Base()
    print(b2.id)

    b3 = Base()
    print(b3.id)

    b4 = Base(12)
    print(b4.id)

    b5 = Base()
    print(b5.id)

