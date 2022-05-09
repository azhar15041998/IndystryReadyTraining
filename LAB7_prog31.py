#31. Write a program to read ten numbers and print their sum by using ‘if’ statement.

num=int(input("Enter numbers to add = "))
result = 0
while num>0:
    digit = num%10  #it will give reminder as last digit
    result = result + digit
    num = num // 10 #truncate division result only interger
print('sum is : ', result)