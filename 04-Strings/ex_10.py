#Problem
#Write a program that captures input from the user.
#Then, swap the letters two at a time in the string.
#The first two characters change places, the third and fourth characters change places, etc. 
#Assume that the user will only input strings with an even number of characters. 
#Important, do not put a prompt when asking for user input.
#Just use input(). Adding a prompt will cause your program to not pass the tests.
'''
Expected Output

    If the user inputs home, then the output is ohem
    If the user inputs cars, then the output is acsr
'''
text = input()
updated_text = ""

for i in range(0,len(text) - 1,2):
    updated_text += text[i + 1] + text[i]
    
                                            
print(updated_text)

