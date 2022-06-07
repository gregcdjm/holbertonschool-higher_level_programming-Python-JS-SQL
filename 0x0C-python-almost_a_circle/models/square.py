#!/usr/bin/python3
""" Base class of all other classes in this project. Manage id attribute
in all future classes and avoid duplicating the same code.
"""

from models.rectangle import Rectangle


class Square(Rectangle):
    """class Square that inherits from Rectangle:
    """

    def __init__(self, size, x=0, y=0, id=None):
        """ __init__ method to create an object instance of the class Rectangle
        """

        super().__init__(size, size, x, y, id)

    def __str__(self):
        """
        The instance method that returns an 'informal' and nicely printable
        string representation of an instance.
        """
        return (f"[square] ({self.id}) {self.x}/{self.y} - {self.width}")

    @property
    def size(self):
        """
       @size.setter method change the data.
       Args:
       - value (int): the width of the rectangle, must be an integer
       """
        return self.width

    @size.setter
    def size(self, value):
        """
        @width.setter method change the data.
        Args:
        - value (int): the width of the rectangle, must be an integer
        """

        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """Update the class square by adding the public method
        def update that assigns an argument to each attribute:
        """
        if args is not None and len(args) != 0:
            for i, value in enumerate(args):
                if i == 0:
                    self.id = value
                elif i == 1:
                    self.size = value
                elif i == 3:
                    self.x == value
                elif i == 4:
                    self.y == value
        else:
            if "id" in kwargs:
                self.id = kwargs["id"]
            if "size" in kwargs:
                self.size = kwargs["size"]
            if "x" in kwargs:
                self.x = kwargs["x"]
            if "y" in kwargs:
                self.y = kwargs["y"]

    def to_dictionary(self):
        """public method def to_dictionary(self): that returns
        the dictionary representation of a square:
        """
        return {
            'id': self.id,
            'x': self.x,
            'size': self.width,
            'y': self.y
        }
