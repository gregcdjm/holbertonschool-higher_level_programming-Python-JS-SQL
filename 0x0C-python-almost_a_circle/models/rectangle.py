#!/usr/bin/python3


from models.base import Base


class Rectangle(Base):
    """class Rectangle that inherits from Base
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """ __init__ method to create an object instance of the class Base
        Args:
            width (_type_): width of the rectangle
            height (_type_): height of the rectangle
            x (int): _description_. Defaults to 0.
            y (int): _description_. Defaults to 0.
            id (_type_): id of the object. Defaults to None.
        """
        if type(height) is not int:
            raise TypeError("width must be an integer")
        if height <= 0:
            raise ValueError("height must be > 0")
        if type(width) is not int:
            raise TypeError("width must be an integer")
        if width <= 0:
            raise ValueError("width must be > 0")
        if x < 0:
            raise ValueError("width must be >= 0")
        if y < 0:
            raise ValueError("width must be >= 0")

        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y
        super().__init__(id)

    @property
    def width(self):
        """
        @property method retrieve the data.
        Return the width of a rectangle
        """
        return self.__width

    @property
    def height(self):
        """
        @property method retrieve the data.
        Return the height of a rectangle
        """
        return self.__height

    @property
    def x(self):
        """
        @property method retrieve the data.
        Return the x
        """
        return self.__x

    @property
    def y(self):
        """
        @property method retrieve the data.
        Return the y
        """
        return self.__y

    @width.setter
    def width(self, value):
        """
        @width.setter method change the data.
        Args:
        - value (int): the width of the rectangle, must be an integer
        """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @height.setter
    def height(self, value):
        """
        @height.setter method change the data.
        Args:
        - value (int): the height of the rectangle, must be an integer
        """
        if type(value) is not int:
            raise TypeError("height must be an integer")
        elif value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @ x.setter
    def x(self, value):
        """
        @x.setter method change the data.
        Args:
        - value (int): the x of the rectangle, must be an integer
        """
        if type(value) is not int:
            raise TypeError("x must be an integer")
        elif value < 0:
            raise ValueError("x must be >= 0")

        self.__x = value

    @ y.setter
    def y(self, value):
        """
        @y.setter method change the data.
        Args:
        - value (int): the y of the rectangle, must be an integer
        """
        if type(value) is not int:
            raise TypeError("y must be an integer")
        elif value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """
        The area method is a public instance.
        Return the current Rectangle area
        """
        return self.__width * self.__height

    def display(self):
        """methond that display the rectangle
        """

        for _ in range(self.__y):
            print()
        for _ in range(self.__height):
            for _ in range(self.__x):
                print(" ", end="")
            for _ in range(self.__width):
                print("#", end="")
            print()

    def __str__(self):
        """
        The instance method that returns an 'informal' and nicely printable
        string representation of an instance.
        """
        return(
            f"[Rectangle] ({self.id}) {self.__x}/{self.__y} -\
                {self.__width}/{self.__height}")

    def update(self, *args, **kwargs):
        """Update the class Rectangle by adding the public method
        def update that assigns an argument to each attribute:
        """
        if args is not None and len(args) != 0:
            for i, value in enumerate(args):
                if i == 0:
                    self.id = value
                elif i == 1:
                    self.__width = value
                elif i == 2:
                    self.__height = value
                elif i == 3:
                    self.__x == value
                elif i == 4:
                    self.__y == value
        else:
            if "id" in kwargs:
                self.id = kwargs["id"]
            if "width" in kwargs:
                self.__width = kwargs["width"]
            if "height" in kwargs:
                self.__height = kwargs["height"]
            if "x" in kwargs:
                self.__x = kwargs["x"]
            if "y" in kwargs:
                self.__y = kwargs["y"]

    def to_dictionary(self):
        """public method def to_dictionary(self): that returns
        the dictionary representation of a Rectangle:
        """
        return {
            'id': self.id,
            'width': self.__width,
            'height': self.__height,
            'x': self.__x,
            'y': self.__y,
        }
