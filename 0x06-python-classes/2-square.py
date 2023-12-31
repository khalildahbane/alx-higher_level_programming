#!/usr/bin/python3

"""Creats a Square class"""


class Square:
    """Represent a square object"""

    def __init__(self, size=0):
        """Initializes an instance of the Square class.

        Args:
            size (int): Size of the square. Defaults to 0.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
