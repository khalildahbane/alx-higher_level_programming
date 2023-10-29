#!/usr/bin/python3
"""writing class"""
import math


class MagicClass:
    """Settings up the class"""

    def __init__(self, radius=0):
        """Settings up the init"""

        self.__radius = 0
        if type(radius) is not int and type(radius) is not float:
            raise TypeError('radius must be a number')
        self.__radius = radius

    def area(self):
        """docstring"""

        return self.__radius ** 2 * math.pi

    def circumference(self):
        """docstring"""

        return 2 * math.pi * self.__radius
