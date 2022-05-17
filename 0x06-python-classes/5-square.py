#!/usr/bin/python3
"""Define a class Square"""


class Square:
    """_summary_
    """
    def __init__(self, size=0):
        """Function that create a square
        Args:
            size (int): size of the square. Defaults to 0.
        """
        self.__size = size

    def area(self):
        """Calculate the current square area
        Returns:
            int: the current square area
        """
        return self.__size ** 2

    @property
    def size(self):
        """getting the size
        Returns:
            int: size of the square
        """
        return self.__size

    @size.setter
    def size(self, value):
        """setting the size
        Args:
            value (int): the new size
        Raises:
            TypeError: exception
            ValueError: exception
        """
        self.__size = value

        if type(value) is not int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")

    def my_print(self):
        """function that prints in stdout the square with the character #
        """
        if self.__size == 0:
            print()
        else:
            for line in range(self.size):
                for colon in range(self.size):
                    print("#", end="")
                print()
