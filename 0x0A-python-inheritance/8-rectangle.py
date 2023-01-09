#!/usr/bin/python3
BaseGeometry = __import__('7-base_geometry').BaseGeometry

"""Rectangle module contains Rectagle class"""


class Rectangle(BaseGeometry):

    def __init__(self, width, height):
        try:
            self.integer_validator("width", width)
            self.integer_validator("height", height)
            self.__width = width
            self.__height = height
        except Exception as e:
            raise e
