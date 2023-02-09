#Problem
#Write a program that accepts input from the user.
#Create another string that contains either a u, l, or - for each character of the original string.
#Use u when the character is uppercase, and use l when the character is lowercase.
#If the character is neither uppercase or lowercase, use -. Print the second string.
#Important, do not put a prompt when asking for user input. Just use input(). Adding a prompt will cause your program to not pass the tests.
    
'''
Expected Output

    If the user inputs cat, then the output will be:

cat
lll

    If the user inputs HouSE, then the output will be:

HouSE
ulluu
'''

text = input()
new_text = ""

for char in text:
    if char.isupper():
        new_text += 'u'
    elif char.islower():
        new_text += 'l'
    else:
        new_text += '-'

print(new_text)



