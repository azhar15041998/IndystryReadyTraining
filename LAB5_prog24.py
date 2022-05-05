#24. Write a program to check whether the given number is positive or negative.

a = int(input('Enter the number :'))
#to check weather given no.is neg or pos lets user if else function 
if a > 0:
    print('The no. is positive')
elif a < 0: #if this conditions is true print the no. is negitive
    print('The no.is negitive')
else:
    print('The number is equals to zero')

    