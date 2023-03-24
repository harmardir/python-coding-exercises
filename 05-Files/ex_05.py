# Problem
# Write a program that reads a tab delimited CSV file and prints the name of the oldest person in the file.


import csv

# open the CSV file for reading
with open('filename.csv', 'r') as file:
    # create a CSV reader object
    reader = csv.reader(file, delimiter='\t')

    # skip the header row
    next(reader)

    # initialize variables for the oldest age and the name of the oldest person
    oldest_age = 0
    oldest_name = ''

    # iterate over each row in the CSV file
    for row in reader:
        # extract the age from the current row
        age = int(row[1])

        # check if the current age is greater than the oldest age seen so far
        if age > oldest_age:
            # update the oldest age and the name of the oldest person
            oldest_age = age
            oldest_name = row[0]

    # print the name of the oldest person
    print(f'The oldest person is {oldest_name} ({oldest_age} years old).')


"""
1-Uses the csv module to read the CSV file. The delimiter argument is set to '\t' to indicate that the file is tab delimited.
2-The with statement is used to automatically close the file when the code is done reading from it.
3-The next() function is used to skip the header row of the CSV file.
4-Variables are initialized to keep track of the oldest age seen so far and the name of the oldest person.
5-A for loop is used to iterate over each row in the CSV file.
6-The age is extracted from the current row and converted to an integer using int().
7-If the current age is greater than the oldest age seen so far, the oldest age and the name of the oldest person are updated.
8-The print() function is used to print the name of the oldest person and their age.

"""
