#!/usr/bin/python3
"""Function that reads a text file (UTF8) and prints it to stdou"""


def read_file(filename=""):
    """Read and print file"""
    with open(filename, encoding="utf-8") as f:
        print(f.read(), end="")
