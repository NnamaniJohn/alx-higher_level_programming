#!/usr/bin/python3

def islower(c):
    if ord(c) in range(97, 124):
        return True
    return False

def uppercase(str):
    for c in str:
        if islower(c):
            print("{}".format(chr(ord(c) - 32)), end="")
        else:
            print(c, end="")
