#!/usr/bin/python3

"""MyList module contains class MyList"""


class MyList(list):
    """
     a class MyList that inherits from list
    """

    def print_sorted(self):
        print(sorted(self))
