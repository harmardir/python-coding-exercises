#Problem

#Write a program that reads a text file and prints the contents in reverse order.

#################################################################################

# open the file for reading
with open('filename.txt', 'r') as file:
    # read the contents of the file and split it into lines
    lines = file.readlines()

# reverse the list of lines
lines.reverse()

# print the reversed lines
for line in lines:
    print(line.rstrip())  # rstrip() removes any newline characters


"""
1-Uses the open() function to open the file for reading. The first argument is the name of the file you want to open, 
  and the second argument is the mode in which you want to open the file ('r' for read mode).
2-The with statement is used to automatically close the file when the code is done reading from it.
3-The readlines() method is used to read the contents of the file into a list called lines, 
  where each element of the list corresponds to a line in the file.
4-The reverse() method is used to reverse the order of the elements in the lines list.
5-A for loop is used to iterate over each element in the lines list in reverse order.
6-The rstrip() method is used to remove any newline characters (\n) from the end of each line before printing it.
"""