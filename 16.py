'''Given the coordinates of two points (x1, y1) and (x2, y2). Write a program to find
the distance between these two points.'''

x1=int(input("enter x1 : "))
x2=int(input("enter x2 : "))
y1=int(input("enter y1 : "))
y2=int(input("enter y2 : "))

#calcualtes distance between two point 
result= ((((x2 - x1 ) ** 2) + ((y2-y1) **2 ) ) **0.5) 

print("distance between",(x1,x2),"and",(y1,y2),"is : ",result)