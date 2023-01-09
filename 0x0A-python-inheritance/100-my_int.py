#!/usr/bin/python3

"""MyInt module"""


class MyInt(int):
    """MyInt class"""

    def __new__(cls, value):
        return  super(MyInt, cls).__new__(cls, value)

    def __eq__(self, other):
        return self > other or self < other

    def __ne__(self, other):
        return not (self > other or self < other)
