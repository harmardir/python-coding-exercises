#Write a program that accepts a 2D list of zeros. Print the 2D list in rows and columns without the square brackets and commas. 
# Moving diagonally from the top-left to the bottom right, replace each 0 with a 1. 
# The IDE already declares the variable number and the 2D list data. Use number to represent the number of rows and columns, 
# and data to represent the 2D list of zeros.

'''
data =  [
            [1, 0, 0],
            [0, 1, 0],
            [0, 0, 1]
          ]
'''
import sys

number = int(sys.argv[1])
data = [[0 for i in range(number)] for j in range(number)]

for row in range(number):
  for column in range(number):
    if row == column:
      data[row][column] = 1
    print(f"{data[row][column]} ", end="")
  print()

