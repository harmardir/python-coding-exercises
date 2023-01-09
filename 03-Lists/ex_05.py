########################################################
# DO NOT EDIT THE CODE IN THE SECTION BELOW
########################################################
import sys

numbers = sys.argv[1:]
for i in range(len(numbers)):
  numbers[i] = int(numbers[i])

########################################################
# Enter your code below
########################################################


for i in range(len(numbers)):
  if numbers[i] % 2 == 0:
    numbers[i] = 'even'
  else:
    numbers[i] = 'odd'


print(numbers)
