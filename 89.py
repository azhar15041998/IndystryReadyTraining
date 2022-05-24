'''
Write a program to print the following triangle.
1 2 3 4 5
1 2 3 4
1 2 3
1 2
1
'''
#let us take the range of 5 lines,step count is -1 to print decreasing order
 
for i in range(5,0,-1):  
    for j in range(1,i+1): 
        print(j,end='') #it print the count of J value
    print()