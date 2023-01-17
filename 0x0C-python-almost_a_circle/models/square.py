#!/usr/bin/python3

"""Square module"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Square class"""

    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)

    def __str__(self):
        return "[Square] ({}) {}/{} - {}".format(self.id, self.x, self.y, self.width)

    @property
    def size(self):
        return self.width

    @size.setter
    def size(self, size):
        self.width = size
        self.height = size

    def update(self, *args, **kwargs):
        if len(args) > 0:
            n = 1
            for arg in args:
                if n == 1:
                    self.id = arg
                if n == 2:
                    self.size = arg
                if n == 3:
                    self.x = arg
                if n == 4:
                    self.y = arg
                n += 1
        else:
            if "id" in kwargs.keys():
                self.id = kwargs["id"]
            if "size" in kwargs.keys():
                self.size = kwargs["size"]
            if "x" in kwargs.keys():
                self.x = kwargs["x"]
            if "y" in kwargs.keys():
                self.y = kwargs["y"]

    def to_dictionary(self):
        dic = {}
        dic.update({"id": self.id})
        dic.update({"size": self.size})
        dic.update({"x": self.x})
        dic.update({"y": self.y})
        return dic
