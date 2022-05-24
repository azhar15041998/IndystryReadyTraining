'''36. Write a program to read the characters continuously until ‘$’ is given and
display the number of characters entered.'''

string =   input("Enter string: ")
char = 0
for i in string:
        char = char+1
        if( i == '$' ):  #if i reaches $ this loop will come out
            break
print("Number of characters entered:")
print(char) 
