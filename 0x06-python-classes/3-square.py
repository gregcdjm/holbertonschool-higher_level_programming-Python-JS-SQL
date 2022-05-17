#!/usr/bin/python3
"""Define a class Square"""


class Square:
    """A Square"""
    def __init__(self, size=0):
        """Function that create a square
        Args:
            size (int): size of the square. Defaults to 0.
        Raises:
            TypeError: exception
            ValueError: exception
        """
        self.__size = size

        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")

    def area(self):
        """calculate the current square area
        Returns:
            int: the current square area
        """
        return (self.__size) ** 2
