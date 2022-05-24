'''Write a program to print the following triangle.
1 1 1 1 1
2 2 2 2
3 3 3
4 4
5
'''
 
for i in range(1,6):  #we have 5 lines ,range takes from 1 to 5 excludes 6
    for j in range(5,i-1,-1): 
        print(i,end='')
    print() #it is same as \n

