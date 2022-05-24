'''
Write a program to print the following triangle.
1
1 1
1 2 1
1 2 3 1
1 2 3 4 1
1 2 3 4 5 1'''
print('1')
for i in range(1,6):   #range is from 1 to 6 since we have 7 lines 
    for j in range(1,i+1): #j values prints in next line increses by 1 
        print(j,end='1')
    print()  #it is same as \n