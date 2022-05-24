'''Write a program to print the following triangle.
1
2 2
3 3 3
4 4 4 4
5 5 5 5 5 '''

for i in range(1,6): #range starts from 1 to 5 excludes 6
    for j in range(1,i+1): #j value increases and prints i value prints in next line
        print(i,end='')
    print()  #it is same as \n
