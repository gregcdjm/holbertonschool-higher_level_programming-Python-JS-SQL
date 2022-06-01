#!/usr/bin/python3
"""the pascal_triangle function"""


def pascal_triangle(n):
    """function that returns a list of lists of integers
    representing the Pascal’s triangle of n"""
    if n <= 0:
        return []
