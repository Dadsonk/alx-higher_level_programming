#!/usr/bin/python3

import random

number = random.randint(-10000, 10000)
temp = number
if number < 0:
    temp = -number
    temp = temp % 10
    temp = -temp
else:
    temp = number % 10
print(f"Last digit of {number:d} is ", end="")
if temp > 5:
    print(f"{temp:d} and is greater than 5")
elif temp == 0:
    print(f"{temp:d} and is 0")
else:
    print(f"{temp:d} and is less than 6 and not 0")
