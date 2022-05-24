'''Write a program to emulate a four-function calculator which can perform
addition, subtraction, multiplication and division. Program should read two real
numbers and an operator which tells the operation to be performed.
'''
a = int(input("Enter First Number: "))
b = int(input("Enter Second Number: "))

print("Enter which operation would you like to perform?")
ch = input("Enter any of these char for specific operation +,-,*,/: ")

if ch == '+':
    result = a + b
elif ch == '-':
    result = a - b
elif ch == '*':
    result = a * b
elif ch == '/':
    result = a / b
else:
    print("please enter valid character")

print(a, ch , b, ":", result)