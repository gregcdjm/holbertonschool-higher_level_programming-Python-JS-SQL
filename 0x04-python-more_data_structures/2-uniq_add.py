#!/usr/bin/python3
def uniq_add(my_list=[]):
    unique = []
    new_list = 0
    for i in my_list:
        if i not in unique:
            unique.append(i)
            new_list += i
    return new_list
