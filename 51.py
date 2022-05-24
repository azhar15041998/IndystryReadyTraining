'''Write a program to display the numbers sequentially from 1 to 99 with 5
numbers on each line.'''

i = 0
for i in range(1,99):#to print 1 to 99 inial value starts from 1
        if i%5==0:
            i = i+5
            print(i,end='')

       
