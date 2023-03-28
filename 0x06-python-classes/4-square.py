#!/usr/bin/python3
<<<<<<< HEAD

"""Define a class Square."""


class Square:
    """Represent a square."""

    def __init__(self, size=0):
        """Initialize a new square.
        Args:
            size (int): The size of the new square.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """Return the current area of the square."""
        return (self.__size * self.__size)
=======
"""A module for working with squares.
"""


class Square:
    """Represents a square with for 4 equal sides
    """
    def __init__(self, size=0):
        """Initializes a Square with a given size.
        """
        if not isinstance(size, int):
            raise TypeError('size must be an integer')
        else:
            if size < 0:
                raise ValueError('size must be >= 0')
            else:
                self.__size = size

    def area(self):
        """Computes the area of this Square.
        Returns:
            int: The area of the Square.
        """
        return self.__size ** 2
>>>>>>> 2276ad50c30a4f134bae58729cfd329eeb95acb3
