#!/usr/bin/python3
"""Defines a Rectangle"""


class Rectangle:
    """Represents a rectangle."""

    def __init__(self, width=0, height=0):
        """Initializes a new Rectangle.

        Args:
            width: this is the width of the new rectangle.
            height: this is the height of the new rectangle.
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """this is the width of the Rectangle which has been set"""
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """this is the height of the Rectangle which has been set"""
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """returns the rectangle area"""
        return (self.__width * self.__height)

    def perimeter(self):
        """returns the rectangle perimeter"""
        if self.__width == 0 or self.__height == 0:
            return (0)
        return ((self.__width * 2) + (self.__height * 2))

    def __str__(self):
        """this will return the printable representation of the Rectangle.

        this represents the rectangle with the # character.
        """
        if self.__width == 0 or self.__height == 0:
            return ("")

        rect = []
        for i in range(self.__height):
            [rect.append('#') for j in range(self.__width)]
            if i != self.__height - 1:
                rect.append("\n")
        return ("".join(rect))
