#Problem
#Write a program that takes input from a user and prints the first character of the input and the last character with some context. 
#Important, do not put a prompt when asking for user input. Just use input(). 
#Adding a prompt will cause your program to not pass the tests.
'''
Expected Output

    If baseball then you will print b is the first character and l is the last character
    If cat then you will print c is the first character and t is the last character

'''

user_input = input()
print(user_input[0] + " is the first character and " + user_input[-1] + " is the last character")

'''
txt = input()
first = txt[0]
last = txt[-1]
print("{} is the first character and {} is the last character".format(first, last))

'''