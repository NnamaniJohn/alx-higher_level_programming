#!/usr/bin/python3

"""add attribute module"""


def add_attribute(obj, name, value):
    """
    function that adds a new attribute to an object
    """
    if hasattr(obj, "__dict__") is False:
        raise TypeError("can't add new attribute")
    setattr(obj, name, value)
