#21. Write a program to print the area of a triangle if b and h values are given.

#To calcualte area of triangle we have 1/2 breadt * height 

breadth = float(input('Enter breadth of the triangle : ')) #takes breadth as input
height = float(input('Enter height of the triangle : '))  #takes height as input
 
#lets apply the formula
Area_of_triangle =  (1 / 2 ) * breadth * height 
print(f'The Area of triangle is   : {Area_of_triangle}')