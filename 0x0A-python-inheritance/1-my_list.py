#!/usr/bin/python3
"""
The print sorted function
"""


class MyList(list):
    """
    Class MyList that inherits from list:
    """

    def print_sorted(self):
        """Print the list sorted
        """
        print(f"{sorted(self)}")
