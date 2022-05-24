#Write a program to find the roots of a given quadratic equation and print the nature of roots

#  quadratic equation ax2 + bx + c = 0,we will take values of a b c from the equation
a = float(input('Enter the value of a :'))
b = float(input('Enter the value of b :'))
c = float(input('Enter the value of c :'))


# The roots are calculated using the formula, x = (-b ± √ (b² - 4ac) )/2a.
r1  = (-b +(b*b - 4*a*c)**0.5)/2*a
r2  = (-b -(b*b - 4*a*c)**0.5)/2*a
print(f'The Roots are R1 :{r1} R2 {r2}')


'''Now we need nature of roots which is calculated using formula of discrement
i,e D = b*b - 4*a*c.'''

d = b*b - 4*a*c

#there are set of conditions to find nature of roots based on d value
if d > 0:  
    print('Two distinct Real Roots')
elif d == 0:
    print("Two Equal Real Roots")
else:
    print("No Roots/Imaginary Roots")



