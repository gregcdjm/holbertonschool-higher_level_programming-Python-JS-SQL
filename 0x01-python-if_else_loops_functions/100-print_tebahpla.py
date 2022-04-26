#!/usr/bin/python3

A = 122
mod = 32
while A >= 65:
    print("{:c}".format(A), end="")
    if A == 65:
        break
    A -= mod + 1
    mod *= -1
