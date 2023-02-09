#Swapping the Case of Characters
#You are going to write a program that takes a string and prints a new string where all of the uppercase letters become lowercase, 
#and the lowercase letters become uppercase.

original_string = "THE BROWN DOG JUMPS over the lazy fox"
modified_string = ""

for char in original_string:
    if char.islower():
        modified_string += char.upper()
    else:
        modified_string += char.lower()

print("The original string is: {}".format(original_string))
print("The modified string is: {}".format(modified_string))
