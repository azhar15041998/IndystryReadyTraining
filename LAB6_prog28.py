#28. Write a program to check whether the given year is leap year or not.

#let us enter the year first 
year = int(input('Enter the year :'))

#a year div by 4 is leap but not with 100 or with 400 ,because every year is not leap year
if year % 4 == 0 and year % 100!= 0 or year % 400 == 0:
    print('The entered year is leap year')
else:
  print('Not a leap year')