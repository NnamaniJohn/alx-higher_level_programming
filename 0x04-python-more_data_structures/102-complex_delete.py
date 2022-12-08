#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    d = []
    for k, v in a_dictionary.items():
        if v == value:
            d.append(k)
    for i in d:
        del(a_dictionary[i])
    return a_dictionary
