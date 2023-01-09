# Slicing a List
#We are going to write a program that takes the middle third of a list and prints it. 
# To keep things simple, we are going to work with list whose length is divisible by 3. 
# The list will also be filled with random integers ranging from 0 to 100.


import random

numbers = []
for i in range(9):
    numbers.append(random.randint(0, 100))

length = len(numbers)
start = length // 3
stop = length // 3 * 2
middle = numbers[start:stop]

print(numbers)
print("The middle is ", middle)
