#!/usr/bin/python3
"""Defines a class Square."""


class Square:
    """represents a square."""

    def __init__(self, size=0):
        """this initializes a new Square.

        Args:
            size (int): this will be the new squares size
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
