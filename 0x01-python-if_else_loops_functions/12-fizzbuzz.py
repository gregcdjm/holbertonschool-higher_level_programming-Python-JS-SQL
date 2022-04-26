while (A < 99)
{
A = A + 1
if (A % (15) == 0)
printf("FizzBuzz ")
else if ((A / 10 + A % 10) % 3 == 0)
printf("Fizz ")
elif ((A % 10 == 5) or (A % 10 == 0))
printf("Buzz ")
else
printf("%d ", A)
}
printf("Buzz\n")
return (0);
}
