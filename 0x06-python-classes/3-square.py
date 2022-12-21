#!/usr/bin/python3
"""This module contains a class that defines a square"""


class Square():
    """Defines a square"""
    def __init__(self, size=0):
        """Initializes a new square
        Args:
            size (int): size of square
        """
        if isinstance(size, int) and size >= 0:
            self.__size = size
        elif not isinstance(size, int):
            raise TypeError('size must be an integer')
        elif (size < 0):
            raise ValueError('size must be >= 0')

    def area(self):
        """Returns the current square area"""
        return self.__size ** 2
