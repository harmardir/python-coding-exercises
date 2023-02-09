#Counting Uppercase and Lowercase Characters
#You are going to write a program that takes a string and prints out two messages. 
#One message tells you how many uppercase characters are in the string. 
#The other messages says how many lowercase characters are in the string. 
#The program will ignore all numbers and special characters (punctuation, symbols, etc.).

lower_count = 0
upper_count = 0
my_string = "Roses are Red, Violets are Blue"

for char in my_string:
    if char.islower():
        lower_count +=1
    elif char.isupper():
        upper_count +=1

print("There are {} lowercase characters.".format(lower_count))
print("There are {} uppercase characters.".format(upper_count))
