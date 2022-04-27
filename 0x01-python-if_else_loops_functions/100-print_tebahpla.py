#!/usr/bin/python3

A = 122
mod = 32
while -mod + 1 + A != 65:
    print("{:c}".format(A), end="")
    A -= mod + 1
    mod *= -1
