#!/usr/bin/python3

"""Creats a Square class based on 3-sequare.py"""


class Square:
    """Represent a square object"""

    def __init__(self, size=0):
        """Initializes sequare"""
        self.__size = size

    @property
    def size(self):
        """"Retrieve size"""
        return self.__size

    @size.setter
    def size(self, value):
        if isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value
        
    def area(self):
        """Return the curruet square area"""
        
        return (self.__size * self.__size)
