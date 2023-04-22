#!/usr/bin/python3
"""Provides a function 'add_integer' that performs integer addition"""


def add_integer(a, b=98):
    """Add two integers"""
    if not isinstance(a, (float, int)):
        raise TypeError("a must be an integer or a float")

    if not isinstance(b, (float, int)):
        raise TypeError("b must be an integer or a float")
    a = int(a)
    b = int(b)
    return a + b
