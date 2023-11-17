#!/usr/bin/python3
def magic_string():
    magic_string.ct = getattr(magic_string, 'ct', 0) + 1
    return ", ".join(["BestSchool" for i in range(magic_string.ct)])
