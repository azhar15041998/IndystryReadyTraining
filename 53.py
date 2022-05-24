''' Write a program to read 9 elements and print the array elements in 3 x 3 matrix
format.'''


#To display 9 elements in 3*3 Matrix Format
r = int(input("Enter the number of rows:"))
c = int(input("Enter the number of columns:"))
matrix = [] #initial matrix
print("Enter the elements of matrix:")
# For user input
for i in range(r): # A for loop for row elements
    a = []
for j in range(c): # A for loop for column elements
    a.append(int(input())) 
matrix.append(a)  #appends add single item to list
# For printing the matrix
for i in range(r):
    for j in range(c):
        print(matrix[i][j], end=" ")
        print()