#Replacing Vowels with a *
#You are going to write a program that takes a string called my_string and returns the string but with a * in the place of vowels. 
#Assume that vowels are a, e, i, o, u. For example, if my_string = "Hello", then your program will print "H*ll*".

my_string = "Hello"
vowels = "aeiou"


for char in my_string:
    if char.lower() in vowels:
        my_string = my_string.replace(char , '*')

print(my_string)