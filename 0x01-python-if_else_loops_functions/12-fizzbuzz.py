#!/usr/bin/python3

for A in range (0, 99):
    if (A % 15) == 0:
        print("FizzBuzz ", end="")
    elif (A / 10 + A % 10) % 3 == 0:
        print("Fizz ", end="")
    elif A % 10 == 5 or A % 10 == 0:
        print("Buzz ", end ="")
    else:
        print(f"{A} ", end ="")
print("Buzz")
