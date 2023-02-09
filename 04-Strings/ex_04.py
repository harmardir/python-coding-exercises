#Count the Vowels
#You are going to write a program that counts the number of vowels that appear in a string. 
#For the purpose of this exercise, vowels are a, e, i, o, u.

my_string = "The Brown Dog Jumps Over The Lazy Fox"
vowels = "aeiou"
count = 0

for char in my_string:
    if char.lower() in vowels:
        count += 1
if count == 1:
    print("There is 1 vowel in the string")
else:
    print("There are {} vowels in the string".format(count))
