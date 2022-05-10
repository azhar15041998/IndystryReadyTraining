'''39. Write a program to check whether the given input is digit or lowercase
character or uppercase character or a special character.
'''
#earlier we have used isupper() islower() now we will user ord()
#ord() returns unicode from a give character 

ch = input('Enter character : ') #reads characters

'''now the unicode for upper ranges from 65 to 90
and for lower 97 to 122 ,and for number 48 to 57'''
#let us apply the above logic in if else

if(ord(ch) >= 65 and ord(ch) <= 90):
	print('Upper')
elif(ord(ch) >= 97 and ord(ch) <= 122):
	print('Lower')
elif(ord(ch) >= 48 and ord(ch) <= 57):
	print('Number')
else:
	print('special Character')

