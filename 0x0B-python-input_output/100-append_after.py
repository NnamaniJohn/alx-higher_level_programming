#!/usr/bin/python3

"""append after"""


def append_after(filename="", search_string="", new_string=""):
    """
    append after
    """
    text = ""
    with open(filename, encoding="utf-8") as myFile:
        while True:
            line = myFile.readline()
            if line == '':
                break
            text += line
            if search_string in line:
                text += new_string

    with open(filename, mode="w", encoding="utf-8") as myFile:
        myFile.write(text)
