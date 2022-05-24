#Write a program to check whether the given alphabet is a vowel or consonant.

#the vowels are 'aeiou'rest are consonets

ch = input('Enter a character : ')
n = 'AEIOUaeiou'
if ch in n:
    print('vowel')
elif ch!=(ord(ch) >= 48 or ord(ch) <= 57): #let us check if input is apart from alphbet we can also check speacial sybols
  print('you have entered a number')
else:
   print('consonet')

#we can also user below method  by cheking each each and every vovel
'''
if ch == 'A'or ch =='a'or ch =='E'or ch =='e'or ch =='I'or ch =='i'or ch =='O'or ch =='o'or ch =='U'or ch =='u':
    print('vovel')
else:
    print('consonent')
'''