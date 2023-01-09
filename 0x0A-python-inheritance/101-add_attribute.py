#!/usr/bin/python3

"""add attribute module"""
def add_attribute(obj, name, value):
    try:
        obj.__setattr__(name, value)
    except Exception:
        raise TypeError("can't add new attribute")
    return
