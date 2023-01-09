#!/usr/bin/python3

"""add attribute module"""
def add_attribute(obj, name, value):
    """
    function that adds a new attribute to an object
    """
    try:
        obj.__setattr__(name, value)
    except Exception:
        raise TypeError("can't add new attribute")
    return
