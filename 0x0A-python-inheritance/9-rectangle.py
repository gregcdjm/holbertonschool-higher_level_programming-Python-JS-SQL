#!/usr/bin/python3
"""Empty class BaseGeometry.
"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """The class Rectangle define:
        * Private instance method: def __init__(self, width, height)
        * the area() method must be implemented
        * print() should print, and str() should return, the following
          rectangle description: [Rectangle] <width>/<height>
    """

    def __init__(self, width, height):
        """
        The initialization method.
        Args:
            - __width (int, private)
            - __height (int, private)
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)

        self.__width = width
        self.__height = height

    def area(self):
        """
        The method area define the area with width * height.
        """
        return (self.__width * self.__height)

    def __str__(self):
        """ The method __str__ print and return the string
         representation of main.
        """
        return(f"[Rectangle] {self.__width}/{self.__height}")
