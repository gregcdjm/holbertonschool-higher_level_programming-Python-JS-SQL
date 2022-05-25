#!/usr/bin/python3
"""Defines a class Rectangle"""


class Rectangle:
    """A Rectangle"""
    def __init__(self, width=0, height=0):
        """init a rectangle

        Args:
            width (int): Defaults to 0.
            height (int): Defaults to 0.
        """
        self.__height = height
        self.__width = width

    @property
    def width(self):
        """
        Function that return the width of the rectangle

        Returns:
            int: width
        """
        return self.__width

    @width.setter
    def width(self, value):
        """Function that set the width value

        Args:
            value (int): must be >= 0
        """
        self.__width = value

        if isinstance(value, int) is False:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")

    @property
    def height(self):
        """
        Function that return the height of the rectangle

        Returns:
            int: height
        """
        return self.__height

    @height.setter
    def height(self, value):
        """Function that set the height value

        Args:
            value (int): must be >= 0
        """
        self.__height = value

        if isinstance(value, int) is False:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")

    def area(self):
        """Function that return the rectangle area

        Returns:
            int: rectangle area
        """
        return self.__height * self.__width

    def perimeter(self):
        """Function that return the rectangle perimeter

        Returns:
            int: perimeter
        """
        if self.__height == 0 or self.__width == 0:
            return 0
        else:
            return (self.__height * 2) + (self.__width * 2)
