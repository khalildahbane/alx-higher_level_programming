#!/usr/bin/python3
"""Defines a square bassed on 6 -square.py"""


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

    @property
    def position(self):
        """Getter/setter property for the position of the square."""
        return (self.__position)

    @position.setter
    def position(self, value):
        if (not isinstance(value, tuple) or
                len(value) != 2 or
                not all(isinstance(i, int) for i in value) or
                not all(i >= 0 for i in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """Return the current square area"""

        return self.__size ** 2

    def my_print(self):
        """set my_print"""

        if self.__size == 0:
            print()
        else:
            for _ in range(self.position[1]):
                print()
            for _ in range(self.size):
                 print(" " * self.position[0] + "#" * self.size)
