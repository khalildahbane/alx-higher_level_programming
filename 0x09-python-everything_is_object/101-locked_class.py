#!/usr/bin/python3
"""defines a lockedclass"""


class LockedClass:
    """ Only allows instatiation of an attribute called first name """

    __slots__ = ["first_name"]
    