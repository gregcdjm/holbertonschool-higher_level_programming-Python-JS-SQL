#!/usr/bin/python3
def uppercase(str):
    for letter in str:
        letter = ord(letter)
        if letter in range(97, 123):
            letter -= 32
        print("{:c}".format(letter), end="")
    print("")
