'''34. Write a program to read a 3-digit number and find whether the middle digit is
numerically equal to the sum of the other two digits and prints an appropriate
response.
'''

num = int(input("Enter a three digit number = ")) #reads 3 digit no.

last = num % 10   # we will get last digit as reminder
first = num // 100 #floor division we will get interger value excludes decimal point since num dev by 100 we will get first value
middle =  num % 100 #to get middle digit  we calculate  reminder first
middle1 = middle // 10 # then floor division ,wll get middle digit
if middle1 == last + first:
    print('middle digit is numberically equal to the addition of first and last digits')
else:
     print('Not equal') 