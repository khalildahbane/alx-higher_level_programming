#!/usr/bin/python3
"""Defines a square bassed on 6 -square.py"""


class Square:
    """Represents a square"""

    def __str__(self):
        """Print the square"""

        return self.pos_print()[:-1]

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
                not all(isinstance(num, int) for num in value) or
                not all(num >= 0 for num in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """Return the current square area"""

        return (self.__size * self.__size)
    
    def pos_print(self):
        """Print the square in position"""

        pos = ""
        if not self.size:
            return "\n"
        for w in range(self.position[1]):
            pos += "\n"
        for w in range(self.size):
            for i in range(self.position[0]):
                pos += " "
            for j in range(self.size):
                pos += "#"
            pos += "\n"
        return pos

    def my_print(self):
        """Print the square in position"""

        print(self.pos_print(), end="")
    