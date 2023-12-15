#!/usr/bin/python3
""" Rectangle Module """
from models.base import Base

class Rectangle(Base):
    """ Rectangle class, inherits from Base """

    def __init__(self, width, height, x=0, y=0, id=None):
        """ Constructor method """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """ Getter method for width """
        return self.__width

    @width.setter
    def width(self, value):
        """ Setter method for width """
        self.validate_integer("width", value)
        self.validate_positive("width", value)
        self.__width = value

    @property
    def height(self):
        """ Getter method for height """
        return self.__height

    @height.setter
    def height(self, value):
        """ Setter method for height """
        self.validate_integer("height", value)
        self.validate_positive("height", value)
        self.__height = value

    @property
    def x(self):
        """ Getter method for x """
        return self.__x

    @x.setter
    def x(self, value):
        """ Setter method for x """
        self.validate_integer("x", value)
        self.validate_non_negative("x", value)
        self.__x = value

    @property
    def y(self):
        """ Getter method for y """
        return self.__y

    @y.setter
    def y(self, value):
        """ Setter method for y """
        self.validate_integer("y", value)
        self.validate_non_negative("y", value)
        self.__y = value

    def validate_integer(self, attribute, value):
        """ Validate if the value is an integer """
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(attribute))

    def validate_positive(self, attribute, value):
        """ Validate if the value is positive """
        if value <= 0:
            raise ValueError("{} must be > 0".format(attribute))

    def validate_non_negative(self, attribute, value):
        """ Validate if the value is non-negative """
        if value < 0:
            raise ValueError("{} must be >= 0".format(attribute))

    def area(self):
        """ Calculate and return the area of the rectangle """
        return self.__width * self.__height

    def display(self):
        """ Display the Rectangle instance with the character #, taking care of x and y """
        for i in range(self.__y):
            print()
        for i in range(self.__height):
            print(" " * self.__x + "#" * self.__width)

    def __str__(self):
        """ Override __str__ method to represent Rectangle object as a string """
        return "[Rectangle] ({}) {}/{} - {}/{}".format(
            self.id, self.__x, self.__y, self.__width, self.__height
        )

    def update(self, *args, **kwargs):
        """ Update attributes with keyworded arguments """
        if args:
            attributes = ["id", "width", "height", "x", "y"]
            for i in range(len(args)):
                setattr(self, attributes[i], args[i])
        elif kwargs:
            for key, value in kwargs.items():
                setattr(self, key, value)

if __name__ == "__main__":
    # Example usage
    r1 = Rectangle(10, 10, 10, 10)
    print(r1)

    r1.update(height=1)
    print(r1)

    r1.update(width=1, x=2)
    print(r1)

    r1.update(y=1, width=2, x=3, id=89)
    print(r1)

    r1.update(x=1, height=2, y=3, width=4)
    print(r1)
def to_dictionary(self):
        """ Return dictionary representation of Rectangle """
        return {"id": self.id, "width": self.width, "height": self.height, "x": self.x, "y": self.y}

# ... (rest of the code)
