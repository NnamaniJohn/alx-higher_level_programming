#!/usr/bin/python3

"""write to file module"""


def write_file(filename="", text=""):
    """
    function that writes a string to a text file (UTF8)
    and returns the number of characters written
    """
    with open(filename, mode="w", encoding="utf-8") as myFile:
        no_lines = myFile.write(text)
        return no_lines
