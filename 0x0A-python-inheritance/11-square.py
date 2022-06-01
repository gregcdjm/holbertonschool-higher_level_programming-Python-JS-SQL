#!/usr/bin/python3
"""the Square class"""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """the Square class"""
    def __init__(self, size):
        """function that create a Square"""
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        """function that return area of a Square"""
        return self.__size ** 2

    def __str__(self):
        """Function that define the __str__ method"""
        return f"[Square] {self.__size}/{self.__size}"
