#!/usr/bin/python3

"""student module"""


class Student:
    """Student class"""

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        if len(attrs) > 0 and type(attrs) == list:
            return dict(filter(lambda ele: ele[0] in attrs,\
                    self.__dict__.items()))
        else:
            return self.__dict__
