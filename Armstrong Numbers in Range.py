# Python Program to Find Armstrong Numbers up to a Limit
n = int(input("Enter the limit: "))

for i in range(n + 1):
    temp = i
    powCount = len(str(i))  # number of digits
    s = 0

    while temp > 0:
        r = temp % 10
        s += r ** powCount
        temp //= 10

    if s == i:
        print(i, end=" ")
