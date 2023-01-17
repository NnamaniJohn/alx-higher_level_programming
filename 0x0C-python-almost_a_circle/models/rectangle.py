#!/usr/bin/python3

"""Rectangle module"""

from models.base import Base


class Rectangle(Base):
    """Rectangle class"""

    def __init__(self, width, height, x=0, y=0, id=None):
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, width):
        if type(width) != int:
            raise TypeError("width must be an integer")
        if width <= 0:
            raise ValueError("width must be > 0")
        self.__width = width

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, height):
        if type(height) != int:
            raise TypeError("height must be an integer")
        if height <= 0:
            raise ValueError("height must be > 0")
        self.__height = height

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, x):
        if type(x) != int:
            raise TypeError("x must be an integer")
        if x < 0:
            raise ValueError("x must be >= 0")
        self.__x = x

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, y):
        if type(y) != int:
            raise TypeError("y must be an integer")
        if y < 0:
            raise ValueError("y must be >= 0")
        self.__y = y

    def area(self):
        return self.width * self.height

    def display(self):
        for i in range(0, self.y):
            print("")
        for i in range(0, self.height):
            for j in range(0, self.x):
                print(" ", end="")
            for j in range(0, self.width):
                print("#", end="")
            print("")

    def __str__(self):
        i = self.id
        x = self.x
        y = self.y
        w = self.width
        h = self.height
        return "[Rectangle] ({}) {}/{} - {}/{}".format(i, x, y, w, h)

    def update(self, *args, **kwargs):
        if len(args) > 0:
            n = 1
            for arg in args:
                if n == 1:
                    self.id = arg
                if n == 2:
                    self.width = arg
                if n == 3:
                    self.height = arg
                if n == 4:
                    self.x = arg
                if n == 5:
                    self.y = arg
                n += 1
        else:
            if "id" in kwargs.keys():
                self.id = kwargs["id"]
            if "width" in kwargs.keys():
                self.width = kwargs["width"]
            if "height" in kwargs.keys():
                self.height = kwargs["height"]
            if "x" in kwargs.keys():
                self.x = kwargs["x"]
            if "y" in kwargs.keys():
                self.y = kwargs["y"]

    def to_dictionary(self):
        dic = {}
        dic.update({"id": self.id})
        dic.update({"width": self.width})
        dic.update({"height": self.height})
        dic.update({"x": self.x})
        dic.update({"y": self.y})
        return dic
