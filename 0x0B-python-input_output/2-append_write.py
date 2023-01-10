#!/usr/bin/python3

"""append file module"""


def append_write(filename="", text=""):
    """
    function that appends a string at the end of a text file (UTF8)
    and returns the number of characters added
    """
    with open(filename, mode="a", encoding="utf-8") as myFile:
        no_lines = myFile.write(text)
        return no_lines
