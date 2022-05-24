'''Write a program to find the second smallest number and its position among
the given ‘n’ numbers.'''

#let us take input in a list
n = input("Enter a list element separated by space ")
list  = n.split()  #split convert string into the list 
 
#now we need to find  smallest number 
list.sort() #list will get sorted 
print(list)
print("Second Smallest element is:", list[1]) #it will print second smallest no.
 
