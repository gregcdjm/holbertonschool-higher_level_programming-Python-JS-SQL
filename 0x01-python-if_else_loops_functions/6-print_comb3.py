#!/usr/bin/python3
a = 0
b = 1

while a < 8:
    print("{}{}".format(a, b), end=", ")
    if b == 9:
        a += 1
        b = a + 1
    else:
        b += 1
print("89")
