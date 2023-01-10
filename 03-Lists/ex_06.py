#Write a program that takes a list of integers called numbers and replaces each element greater than 10 with a '*'. 
# Print the new version of numbers.
#Expected Output
#If numbers = [30, 1, 20, 4] then you will print ['*', 1, '*', 4]
#If numbers = [5, 9, 11, 23] then you will print [5, 9, '*', '*']

numbers = [30, 1, 20, 4] 

for i in range(len(numbers)):
  if numbers[i] > 10:
    numbers[i] = '*'


print(numbers)
