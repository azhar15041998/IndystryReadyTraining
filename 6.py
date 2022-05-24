#6. Write a program to find the area and circumference of a circle.

radius = float(input('Enter radius of the circle : ')) #User inputs the radius.
pi = 3.14                                           #The pi value is 3.14 
Area = pi * radius * radius                         #Area of circle is pi r**2 
Circumfernce = 2 * pi * radius                      #circomference formula 2 pi*r
print(f'The Area of circle is : {Area} \nThe Circumference of Circle is : {Circumfernce}') #Prints Area and circumfernece
