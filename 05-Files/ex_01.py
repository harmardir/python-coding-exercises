
#Problem
#Write a program that reads a text file and returns the number of lines as well as the total number of characters in the file.

import sys

test_file = sys.argv[1]

line_count = 0
char_count = 0

with open(test_file, "r") as input_file:
    line = input_file.readline()
    while line != "":
        line_count += 1
        char_count += len(line)
        line = input_file.readline()

print("{} lines".format(line_count))
print("{} characters".format(char_count))