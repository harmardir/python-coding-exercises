# Coding Sum
#Python already has a sum function, but we are going to write some code that manually calculates the sum of a list.


import random

numbers = []
total = 0

for i in range(20):
    numbers.append(random.randint(0, 100))

for number in numbers:
    total += number

print("The sum of numbers is ", total)
print(sum(numbers))