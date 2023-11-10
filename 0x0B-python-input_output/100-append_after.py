#!/usr/bin/python3
"""
Defines a text file insertion function
"""


def append_after(filename="", search_string="", new_string=""):
    """Insert text after each line containing a given string in a file"""
    with open(filename, 'r') as file:
        lines = file.readlines()

    with open(filename, 'w') as file:
        for line in lines:
            file.write(line)
            if search_string in line:
                file.write(new_string)

