'''Write a program to print the numbers which are divisible by both 3 and 7 from
1 to 100.
'''

for i in range(1,100):  #range from 1 to 100, excludes 100
        if (i % 3 == 0 and i % 7 == 0): #condition for div by both 3 annd 7 
            print(i) #print the value after evaluating above condition