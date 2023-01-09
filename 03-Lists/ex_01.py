# Odd or Even
#Here is how you can iterate through a list, determine if the number is odd or even, 
# and then put that number in a list of odd or even numbers. After the program has run, 
# all of the odd numbers will be in the odd list and all of the even numbers will be in the even list.

import random

numbers = []
for i in range(20):
    numbers.append(random.randint(0, 100))
    
odd = []
even = []

for number in numbers:
    if number % 2 == 0:
        even.append(number)
    else:
        odd.append(number)

print("The odd numbers: ", odd)
print("The even numbers: ", even)
print(len(odd) + len(even))