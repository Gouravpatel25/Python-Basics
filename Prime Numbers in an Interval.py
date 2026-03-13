#Python Program to Print all Prime Numbers in an Interval
import math
n = int(input("Enter the lower limit: "))
m = int(input("Enter the upper limit: "))


for i in range(n,m):
    flag = True
    if(i<=1):
       flag= False
    else:
        limit = int(math.sqrt(i))
        for j in range(2, limit+1):
            if(i%j == 0):
                flag = False
                break

    if(flag):
        print(i, end=" ")
