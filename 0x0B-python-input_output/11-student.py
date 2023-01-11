#!/usr/bin/python3

"""student module"""


class Student:
    """Student class"""

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        if attrs is not None:
            d = dict(filter(lambda e: e[0] in attrs, self.__dict__.items()))
            return d
        else:
            return self.__dict__

    def reload_from_json(self, json):
        self.__dict__.update(json)
