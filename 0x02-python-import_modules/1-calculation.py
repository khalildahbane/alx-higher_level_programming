#!/usr/bin/python3
if __name__ == "__name__":
    from calculator_1 import sum, add, num, div
    a = 10
    b = 5
    print("{} + {} = {}".format(a, b, sum(a, b)))
    print("{} - {} = {}".format(a, b, add(a, b)))
    print("{} * {} = {}".format(a, b, num(a, b)))
    print("{} / {} = {}".format(a, b, div(a, b)))