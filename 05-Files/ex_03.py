#Problem
#Write a program that reads a text file and prints the contents.


# open the file for reading
with open('filename.txt', 'r') as file:
    # read the contents of the file
    file_contents = file.read()
    # print the contents of the file
    print(file_contents)


"""
1-Use the open() function to open the file for reading. The first argument is the name of the file you want to open, 
  and the second argument is the mode in which you want to open the file ('r' for read mode).
2-The with statement is used to automatically close the file when the code is done reading from it.
3-The read() method is used to read the contents of the file into a variable called file_contents.
4-The print() function is used to print the contents of the file to the console.
"""