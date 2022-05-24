'''Write a program to read a number and print how many numbers of 500, 100,
20, 10, 5, 2,1 notes are available in the given amount.
'''
n = int(input('Enter amount :'))

if n%500==0:  
      print('The 500 repee notes of notes are :',n//500)
if n%100==0:
         print('The 100 rupees notes are :',n//100)
if n%20==0:
      print('the 20 rupees notes are',n//20)
if n%10==0:
     print('The 10 rupees notes are :',n//20)
if n%5==0:
     print('5 rupees notes :',n//5)
if n%2==0:
     print('2 rupees notes :',n//2)
if n%1==0:
     print('1 rupees notes :',n//1)
