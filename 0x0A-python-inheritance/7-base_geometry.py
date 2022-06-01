#!/usr/bin/python3
"""the BaseGeometry class"""


class BaseGeometry:
    """the BaseGeometry class"""

    def area(self):
        """function that raise an exception"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """function that validates value"""
        if type(value) is not int:
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
