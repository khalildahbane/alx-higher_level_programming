#!/usr/bin/python3

"""Defines a base model class."""
import json
import csv
import turtle

class base:
    """Base model for all other classes in project"""


    __nb_objects = 0

    def __init__(self, id=None):
        """"Initialize a new Base"""

        if id is not None:
            slef.id = id
        else:
            base.__nb_objects += 1
            self.id = base.__nb_objects
