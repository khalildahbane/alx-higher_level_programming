#!/usr/bin/python3
"""This module inherits from the list class"""


class Mylist(list):
    """a Public instance class"""

    def print_sorted(self):
        """print a sorted list"""

        print(sorted(self))
