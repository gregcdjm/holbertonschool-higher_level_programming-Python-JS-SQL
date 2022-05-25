#!/usr/bin/python3
"""
function add_integer
"""


def add_integer(a, b=98):
    """
    function that add 2 integers

    Args:
        a (int or float): cast to int
        b (int or float): cast to int

    Returns:
        int: addition of a and b
    """
    if isinstance(a, (int, float)) is False:
        raise TypeError("a must be an integer")
    elif isinstance(b, (int, float)) is False:
        raise TypeError("b must be an integer")
    return int(a) + int(b)
