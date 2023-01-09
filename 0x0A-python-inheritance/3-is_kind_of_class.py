#!/usr/bin/python3

"""is kind of class module contains one function is_kind_of_class"""


def is_kind_of_class(obj, a_class):
    """
    a function that returns True if the object is
    an instance of, or if the object is an instance of a class
    that inherited from, the specified class ; otherwise False.
    """
    return issubclass(type(obj), a_class)
