#!/usr/bin/python3

"""Rectangle module contains Rectagle class"""

BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """A Rectangle class"""

    def __init__(self, width, height):
        try:
            self.integer_validator("width", width)
            self.integer_validator("height", height)
            self.__width = width
            self.__height = height
        except Exception as e:
            raise e

    def area(self):
        return self.__width * self.__height

    def __str__(self):
        return "[Rectangle] {}/{}".format(self.__width, self.__height)
