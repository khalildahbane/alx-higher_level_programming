#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    new_dir = a_dictionary.copy()
    list_keys = list(new_dir.keys())

    for a in list_keys:
        new_dir[a] *= 2

    return (new_dir)
