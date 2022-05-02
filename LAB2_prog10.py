#10. Write a program to find the simple interest and compound interest.
principal = float(input("Enter principle Amount : "))
tenure = float(input("Enter Tenurity in Years : "))
rate_of_interest = float(input("Enter   Rate of interest : "))

#calculates simple interest  
simple_interest = (principal * tenure * rate_of_interest) / 100
print(f'The simple interest is : {simple_interest}"')

#calculates compound interest
ci =  principal * (((1 + rate_of_interest / 100) **tenure)) 
print(f'The Compound interest is : {ci}"')


