#27. Write a program to find biggest of given three numbers.

a = int(input('Enter the number a : '))
b = int(input('Enter the number b : '))
c = int(input('Enter the number c : '))

#lets check biggest among three numbers using if 
if a > b and a > c:
    print('A is bigger')
elif b > a and b > c:
    print('B is bigger')
else:
    print('C is bigger')