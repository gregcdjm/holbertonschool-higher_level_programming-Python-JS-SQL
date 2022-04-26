#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)

last_digit = number % 10

if number < 0:
    last_digit = (-1 * number) % 10
    last_digit *= -1
else:
    last_digit = number % 10
print("Last digit of {number} is {last_digit} and is")
if last_digit == 0:
    print(" greater than 5")
elif last_digit > 5:
    print(" 0")
else :
    print(" less than 6 and not 0")
