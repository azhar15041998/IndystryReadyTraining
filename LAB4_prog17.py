'''Rajesh’s basic salary is input through the keyboard. His D.A. is 40% of basic
salary, and H.R.A. is 20% of basic salary. Write a program to calculate his
gross salary'''

Basic_salary = float(input("Enter Basic salary : ")) #It take basic salary as input

#give Dearness allowances is 40 % of Basic salary and HRA is 20% of Basic salary
DA = Basic_salary * 0.4
HRA = Basic_salary * 0.2
Gross_Salary = (Basic_salary + DA + HRA)
print('The Gross Salary is :' , Gross_Salary)

