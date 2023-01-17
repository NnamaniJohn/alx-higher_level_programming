#!/usr/bin/python3

"""Base module"""
import json


class Base:
    """Base class"""

    __nb_objects = 0

    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            type(self).__nb_objects += 1
            self.id = type(self).__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        if list_dictionaries is None:
            list_dictionaries = []
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        if list_objs is None:
            list_objs = []
        list_dic = []
        for ins in list_objs:
            list_dic.append(ins.to_dictionary())
        with open("{}.json".format(cls.__name__), mode="w",\
                encoding="utf-8") as myFile:
            myFile.write(cls.to_json_string(list_dic))
        return

    @staticmethod
    def from_json_string(json_string):
        if json_string is None:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        dummy = cls(10, 10)
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        with open("{}.json".format(cls.__name__), encoding="utf-8") as myFile:
            text = myFile.read()
        if text == "" or text is None:
            text = "[]"
        list_dic = cls.from_json_string(text)
        list_obj = []
        for dic in list_dic:
            list_obj.append(cls.create(**dic))
        return list_obj
