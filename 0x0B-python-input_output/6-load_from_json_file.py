#!/usr/bin/python3

"""load from json file"""
import json


def load_from_json_file(filename):
    """
    function that creates an Object from a “JSON file”
    """
    with open(filename, encoding="utf-8") as myFile:
        text = myFile.read()
    return json.loads(text)
