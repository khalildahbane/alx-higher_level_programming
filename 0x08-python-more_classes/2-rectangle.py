#!/usr/bin/python3
"""Defines a rectangle"""


class Rectangle:
    """Defines a rectangle based on 1-rectangle.py"""

    def __init__(self, width=0, height=0):
        """Initializes a rectangle with width and height"""

        self.width = width
        self.height = height

    @property
    def width(self):
        """Set width attribute"""

        return self.__width

    @width.setter
    def width(self, value):
        """Set width attribute"""

        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")

        self.__width = value

    @property
    def height(self):
        """Set height attribute"""

        return self.__height

    @height.setter
    def height(self, value):
        """Set height attribute"""""

        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")

        self.__height = value

        def area(self):
            """returns instance method"""

            return self.width * self.height
        
        def perimeter(self):
            """"Return perimeter method"""

            return 2 * (self.width + self.height)
