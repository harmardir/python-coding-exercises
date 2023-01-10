# Changing a List
#Write a program that takes a list of integers called numbers and will print a
#list with the elements odd or even based on the elements of numbers. 
# For example, if numbers = [1, 2, 3, 4], then your program will print ['odd','even', 'odd', 'even'].

numbers = [1, 2, 3, 4]

for i in range(len(numbers)):
  if numbers[i] % 2 == 0:
    numbers[i] = 'even'
  else:
    numbers[i] = 'odd'


print(numbers)
