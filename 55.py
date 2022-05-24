#55. Write a program to find the biggest of the given numbers.

#lets takes elements in list 
 
n = input("Enter a list element separated by space ")
list  = n.split()  #split convert string into the list 
print(list)
print('the greatest no.  is ',max(list))  #  max() to print greatest of all no.s