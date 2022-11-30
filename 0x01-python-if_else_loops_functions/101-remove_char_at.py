#!/usr/bin/python3
def remove_char_at(str, n):
    i = 0
    s = ""
    for c in str:
        if i != n:
            s = s + c
        i += 1
    return s
