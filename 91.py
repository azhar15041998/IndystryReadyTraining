'''
Write a program to print the following triangle.
5 5 5 5 5
4 4 4 4
3 3 3
2 2
1
'''

for i in range(6,1,-1): #we have 5 lines ,range takes from 1 to 5 excludes 6 with decreament
    for j in range(1,i+1):
        print(j,end='')
        j+=1
    print()
