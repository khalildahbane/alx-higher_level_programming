#!/usr/bin/python3
"""An class based on 6-base_geometry.py"""


class BaseGeometry:
    """This class  represents a base geometry"""

    def area(self):
        """not implemented"""

        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """validates a value as an integer"""

        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
