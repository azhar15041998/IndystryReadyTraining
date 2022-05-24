''' Write a program to read positive numbers continuously until negative number
is given by using ‘if’.'''

num = float(input("Enter a number: "))
if num > 0:
   print("Read No")
elif num == 0:
   print("Zero")
else:
   print("Stop Reading")