# Author: Ileana Hernandez
# Date: 01/27/2021
# Description: Fibonacci sequence

def fib(n):
    """takes a positive integer and returns the number at that
    position of the Fibonacci sequence"""

    a = 0
    b = 1
    if n < 0:
        print("Invalid input")
    elif n == 0:
        return a
    elif n == 1:
        return b
    else:
        for i in range (2, n+1):
            c = a + b
            a = b
            b = c
        return b

print(fib(11))
print(fib(17))