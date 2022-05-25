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
        self.height = height
        self.width = width

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
        if isinstance(value, int) is False:
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

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
        if isinstance(value, int) is False:
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
