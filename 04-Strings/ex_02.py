#Reverse a String
#You are going to write a program that takes a string and prints it in reverse order.

my_string = "The brown dog jumps over the lazy fox"
reversed_string = ""

index = len(my_string) - 1
while index >= 0:
    reversed_string += my_string[index]
    index -= 1

print(reversed_string)