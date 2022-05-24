'''86. Write a program to print the following triangle.
1
1 2
1 2 3
1 2 3 4
1 2 3 4 5
'''
#let us initize with1 

for i in range(1,6): #range starts from 1 to 5 excludes 6
    for j in range(1,i+1):
        print(j ,end='')
    print() #it is same as \n
 