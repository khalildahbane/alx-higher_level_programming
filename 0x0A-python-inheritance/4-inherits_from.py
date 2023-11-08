#!/usr/bin/python3
"""A function that returns True if the object is an instance otherwise False"""


def  inherits_from(obj, a_class):
    """This function returns true if object is an instance otherwise False"""

    return (issubclass(type(obj), a_class) and type(obj) != a_class)
