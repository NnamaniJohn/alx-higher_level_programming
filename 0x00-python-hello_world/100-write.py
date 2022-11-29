#!/usr/bin/python3
import os
import sys

s = "and that piece of art is useful - Dora Korpar, 2015-10-19\n"
line = str.encode(s)
os.write(2, line)
sys.exit(1)
