#!/usr/bin/python3
"""Defines a class Student"""


class Student:
    """Represent a student"""

    def __init__(self, first_name, last_name, age):
        """Initializes a new Student"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Get a dictionary representation of the Student"""
        if (isinstance(attrs, list) and
                all(isinstance(x, str) for x in attrs)):
            return ({x: y for x, y in self.__dict__.items() if x in attrs})
        else:
            return self.__dict__

    def reload_from_json(self, json):
        """Replace all attributes of the Student"""
        if (json):
            self.__dict__ = json

