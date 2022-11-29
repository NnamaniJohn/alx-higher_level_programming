#!/usr/bin/python3

def islower(c):
    if ord(c) in range(97, 124):
        return True
    return False


def uppercase(str):
    for c in str:
        if islower(c):
            c = chr(ord(c) - 32)
        print("{}".format(c), end="")
    print("\n")
