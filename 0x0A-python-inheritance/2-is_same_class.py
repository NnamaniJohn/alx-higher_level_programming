#!/usr/bin/python3

"""same class module contains one function is_same_class"""


def is_same_class(obj, a_class):
    """
    function that returns True if the object is exactly
    an instance of the specified class ; otherwise False.
    """
    return type(obj) is a_class