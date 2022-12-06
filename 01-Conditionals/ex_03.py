"""
Problem
---------
Use the variable x as you write this program. x will represent a positive integer. 
Write a program that determines if x is divisible by 5 and even. 
If yes, print _ is divisible by 5 and even, where the blank is the value of x.
 If no, print _ is not divisible by 5 or it is odd, where the blank is the value of x.

"""

x = 35

if (x % 5 == 0) and (x % 2 == 0):
    print(str(x) + " is divisible by 5 and even")
else:
    print(str(x) + " is not divisible by 5 or it is odd")
