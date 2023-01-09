#!/usr/bin/python3

"""square module contains class Square"""

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """A Square class"""

    def __init__(self, size):
        try:
            self.integer_validator("size", size)
            super().__init__(size, size)
            self.__size = size
        except Exception as e:
            raise e

    def area(self):
        return self.__size * self.__size
