#!/usr/bin/python3

def fizzbuzz()

for A in range (1, 100):
    if (A % 15) == 0:
        print("FizzBuzz ", end="")
    elif (A % 3) == 0:
        print("Fizz ", end="")
    elif A % 10 == 5 or A % 10 == 0:
        print("Buzz ", end ="")
    else:
        print(f"{A} ", end ="")
print("Buzz ")
