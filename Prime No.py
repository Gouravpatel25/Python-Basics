# Python Program to Check if a Number is Prime or Not
import math

n = int(input("Enter a number to check: "))

if n <= 1:
    print("Invalid input")
else:
    limit = int(math.isqrt(n))
    is_prime = True
    for i in range(2, limit + 1):
        if n % i == 0:
            is_prime = False
            break
    if is_prime:
        print("Prime number")
    else:
        print("Not Prime number")
