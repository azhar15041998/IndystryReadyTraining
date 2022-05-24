#22. Write a program to print the area of a triangle if three sides are given.
#let us enter 3 sides of triangle 
a = float(input('Enter side 1 of triangle '))
b = float(input('Enter side 2 of triangle '))
c = float(input('Enter side 3 of triangle '))

#now the semi-perimeter of the triangle, i.e., s = (a + b + c)/2.
s = (a + b + c)/2

#now We will find the area of the triangle using the Heron's formula. 
 
Area = (s*(s-a)*(s -b)*(s-c)) ** (1/2)
print("The Area of the triangle when 3 sides are give is  : ", Area)