#Write a program that takes a list called strings that contains a random selection of strings. 
# Your program should print the first string when arranged in alphabetical order.
#Expected Output
#If strings = ['luck', 'cat', 'kid', 'house'] then you will print cat
#If strings = ['duck', 'dddd', 'mouse', 'kite'] then you will print dddd



strings = ['luck', 'cat', 'kid', 'house']

strings.sort()
print(strings[0])
