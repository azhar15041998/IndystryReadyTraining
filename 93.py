'''
Write a program to print the following triangle
5
5 4
5 4 3
5 4 3 2
5 4 3 2 1
'''
 
for i in range(6,0,-1): #range starts from 1 to 5 excludes 6
    for j in range(5,i-1,-1): #j value decreased and prints j value prints in next line
        print(j,end='')
        
print() #it is same as \n
