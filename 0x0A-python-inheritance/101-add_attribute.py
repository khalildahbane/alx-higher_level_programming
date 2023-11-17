#!/usr/bin/python3
""" Function to add attribute to dictionary"""


def add_attribute(object, attribute, value):
    """This function adds attributes to objects"""

    if not hasattr(object, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(object, attribute, value)
