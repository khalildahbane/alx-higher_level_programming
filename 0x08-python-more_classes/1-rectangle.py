#!/usr/bin/python3
"""defines a rectangle based on 0-rectangle.py"""


class Rectangle:
    """empty class Rectangle"""

    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height
    
    @property
    def width(self):
        """Set width attribute"""
                
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise TypeError("width must be >= 0")
        return value
    
    @property
    def height(self):
        """Set height attribute"""
        
        return self.__height
    
    @width.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value <= 0:
            raise TypeError("height must be >= 0")
        return value

def __str__(self):
        return f"Rectangle({self.width}, {self.height})"
        return self.width * self.height
