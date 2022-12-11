"""
Create a nested loop that produces the output below.


....1
...2
..3
.4
5

"""

i = 0
j = 5
for i in range(6):
  while j > 0: 
    j = j - 1 
    i = i + 1
    print('.' * j + str(i))

##############################################

for num in range(1,6):
  for dots in range(5-num, 0, -1):
    print(".", end='')
  print(num)