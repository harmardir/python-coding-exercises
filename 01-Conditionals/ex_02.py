"""
Problem
---------
Use the variable x as you write this program. x will represent a positive integer. 
Write a program that determines if x is divisible by 5. If yes, print _ is divisible by 5, 
where the blank is the value of x. If no, print _ is not divisible by 5, 
where the blank is the value of x.

"""

x = 18

if x % 5 == 0:
    print(str(x) + " is divisible by 5")
else:
    print(str(x) + " is not divisible by 5")
