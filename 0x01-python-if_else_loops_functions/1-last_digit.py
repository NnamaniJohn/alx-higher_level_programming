#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number < 0:
    n = number * -1
else:
    n = number
if n % 10 > 5:
    print(f"Last digit of {number:d} is {n % 10} and is greater than 5")
elif n % 10 == 0:
    print(f"Last digit of {number:d} is {n % 10} and is 0")
else:
    print(
    f"Last digit of {number:d} is {n % 10} and is less than 6 and not 0")
