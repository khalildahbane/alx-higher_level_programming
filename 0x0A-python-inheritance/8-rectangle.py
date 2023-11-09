#!/usr/bin/python3
"""An class based on 7-base_geometry.py"""


class BaseGeometry:
    """This class represents a base geometry"""

    def integer_validator(self, name, value):
        """validates a value as an integer"""

        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))

class Rectangle:
    """this class inherits from BaseGeometry"""

    def __init__(self, width, height):
        """Intialize a new Rectangle"""

        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
