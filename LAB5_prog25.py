#25. Write a program to find out the given number is odd or even.

a = int(input('Enter the number :'))

#if the entered no. is results reminder 0 is even eles odd
#let us make it with if else statement 
if (a % 2 ) == 0:
    print('The entered number is EVEN ')
else:
    print('The entered number is ODD ')