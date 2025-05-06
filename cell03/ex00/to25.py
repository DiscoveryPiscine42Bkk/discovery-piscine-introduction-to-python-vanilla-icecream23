#!/usr/bin/env python3
i = int(input("Enter a number : "))
if i < 25:
    while i <= 25:
        print("Inside the loop, my variable is",i)
        i += 1 
else:
    print("ERROR")
    