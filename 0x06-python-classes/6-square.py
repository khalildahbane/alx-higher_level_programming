#!/usr/bin/python3
"""Defines a square bassed on 5 -square.py"""


class Square:
    """Represents a square"""

    def __init__(self, size=0, posistion=(0, 0)):
        """Initializes the data"""

        self.size = size
        self.position = posistion

    @property
    def size(self):
        """Retrieve size"""

        return self.__size

    @size.setter
    def size(self, value):
        """Sets Size"""

        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >=0")
        self.__size = value

    @position.setter
    def position(self):
        """set the position of this Square"""
        self.position
    
    @position.setter
    def position(self, value):
        if not isinstance(value, tuple):
            raise TypeError('position must be a tuple of 2 positive integers')
        if len(value) != 2:
            raise TypeError('position must be a tuple of 2 positive integers')
        if len([i for i in value if isinstance(i, int) and i >= 0]) != 2:
            raise TypeError('position must be a tuple of 2 positive integers')
        self.position = value

    def area(self):
        """Return the current square area"""

        return (self.__size * self.__size)

    def my_print(self):
        """set my_print"""

        if self.__size == 0:
            print()
            return
        
        [print("") for i in range(0, self.position[1])]
        for i in range(0, self.__size):
            [print(" ", end="") for j in range(0, self.position[0])]
            [print("#", end="") for k in range(0, self.__size)]
            print("")
