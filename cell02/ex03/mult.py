#!/usr/bin/env python3
x = int(input("Enter the first number : "))
y = int(input("Enter the second number : "))
z = x * y
print(x,"x",y,"=",z)
if z > 0:
    print("The result is postive")
elif z < 0:
    print("The result if negative")
else:
    print("The result if postive and negative")
