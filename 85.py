
#85. Write a program to print the Floyd’s triangle.
'''
1
2 3
4 5 6
7 8 9 10
'''
c = 1  #initializing to 1 since need to start from 1

for i in range(1, 5):  #range will be 1 to 4 it excludes 5 since we need 4 lines
    for j in range(1, i+1): #next line will be increamented
        print(c, end=' ') 
        c += 1 #the count increases by line for every element as per command in above
    print()