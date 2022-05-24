'''Write a program to read a character and find out whether it is uppercase or
lowercase'''

#this can be done useing isupper() and islower() and also with ord() function
#let us read the character
ch = input('Enter a character :')

if ch.isupper():      #isupper function checks for uppercase
    print('The entered character is in upper case ')
elif ch.islower():    #islower function checks for uppercase
    print('The entered character is in Lower case ')
else:
    print('Not an alphabet')
