#!/usr/bin/python3
def search_replace(my_list, search, replace):
    new_list = list(map(lambda b: replace if b == search else b, my_list))
    return (new_list)