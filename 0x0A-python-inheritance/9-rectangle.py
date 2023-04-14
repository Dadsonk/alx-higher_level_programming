#!/usr/bin/python3

"""
contains the class BaseGeometry and subclass Rectangle
BaseGeometry (class): inheriting from the BaseGeometry class
    Args:
        -width: width property of the rectangle
        -height: height property of the rectangle
"""



BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
   	"""
	A representation of a rectangle
	"""
    def __init__(self, width, height):
        """
	instantialize the rectangle
	"""
        self.__width = width
        self.__height = height
        BaseGeometry.integer_validator(self, "width", self.__width)
        BaseGeometry.integer_validator(self, "height", self.__height)



    def area(self):
        return self.__width * self.__height

    def __str__(self):
        """print"""
        return ("[Rectangle] " + str(self.__width) + "/" + str(self.__height))
