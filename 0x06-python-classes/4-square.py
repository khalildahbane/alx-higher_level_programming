#!/usr/bin/python3

"""Creats a Square class based on 3-sequare.py"""


class Square:
    """Represent a square object"""

    def __init__(self, size=0):
        """Initializes sequare"""
        self.squaer = size
    
    def size(self):
        """"Retrieve size"""
        return self.squaer
    
    def size(self, value):
        if isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise TypeError("size must be >= 0")
        self.squaer = value
        
    def area(self):
        return (self.__size * self.__size)
