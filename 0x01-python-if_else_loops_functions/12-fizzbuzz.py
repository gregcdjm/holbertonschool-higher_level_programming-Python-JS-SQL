#!/usr/bin/python3
def fizzbuzz():

    for A in range(1, 101):
        if (A % 15) == 0:
            print("FizzBuzz ", end="")
        elif (A % 3) == 0:
            print("Fizz ", end="")
        elif A % 5 == 0:
            print("Buzz ", end="")
        else:
            print(f"{A} ", end="")
