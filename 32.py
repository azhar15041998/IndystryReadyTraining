'''Write a program to read three sides a, b, c of a triangle and print the type of
the triangle.'''


a = int(input("Enter first side : "))
b = int(input("Enter second side : "))
c = int(input("Enter third side : "))

if a == b and b == c :
    print("Equilateral Triangle")  #three sides are equal
elif a == b or b == c or c == a: #two sides are equal
    print("Isosceles Triangle")
else :
    print("Scalene Triangle")   #three sides are different