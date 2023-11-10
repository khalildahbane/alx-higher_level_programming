#!/usr/bin/python3
"""Function that reads a text file (UTF8) and prints it to stdou"""


def read_file(filename=""):
    """Read and print file"""

    with open(filename, "r" encoding="UTF-8") as file:
    print (file.read(), end="")