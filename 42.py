#Write a program to find the oldest and youngest among 3 people.

a = int(input('Enter the age of a : '))
b = int(input('Enter the age of b : '))
c = int(input('Enter the age of c : '))

#lets check biggest among three numbers using if 
if a > b and a > c:
    print('A is oldest')
elif b > a and b > c:
    print('B is oldest')
else:
    print('C is oldest')