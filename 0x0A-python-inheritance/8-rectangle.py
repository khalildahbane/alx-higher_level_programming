#!/usr/bin/python3
"""Inheris from baseGeometry 7-base_geometry.py"""


class BaseGeometry:
    """This class represents a base geometry"""

    def integer_validator(self, name, value):
        """validates a value as an integer"""

        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))


class Rectangle(BaseGeometry):
    """this class inherits from BaseGeometry"""

    def __init__(self, width, height):
        """Intialize a new Rectangle"""

        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height
