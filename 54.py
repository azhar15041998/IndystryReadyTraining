#54. Write a program to display the multiplication table for a given number.

a = int(input('Enter Number :'))

for i in range(1,11): #iterates 1 to 10
    print(a ,'*',i ,'=' ,a*i) #enter numbers multiplis with range till 10 then stops iteration
    