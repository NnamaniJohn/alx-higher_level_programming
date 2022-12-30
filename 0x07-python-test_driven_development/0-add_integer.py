#!/usr/bin/python3

"""
This is the "add integer" module.

The example module supplies one function, add_integer().
"""
def add_integer(a, b=98):
    """
    function that adds 2 integers
    """
    if not (type(a) == int or type(a) == float):
        raise TypeError("a must be an integer")
    if not (type(b) == int or type(b) == float):
        raise TypeError("b must be an integer")
    return int(a) + int(b)
