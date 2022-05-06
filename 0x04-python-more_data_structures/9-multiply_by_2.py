#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    new_a_dictionary = a_dictionary.copy()
    for value in a_dictionary:
        new_a_dictionary[value] = a_dictionary[value] * 2
    return new_a_dictionary
