'''35. A Company insures its drivers in the following cases.
1. If the driver is married.
2. If the driver is unmarried, male and above 30 years of age.
3. if the driver is unmarried, female and above 25 years of age.
In all other cases, the driver is not insured. If the marital status, sex, age of the
driver are the inputs, write a program to determine whether the driver is insured or not '''

marital_status = input('Enter marital status: ')
sex = input('Enter gender: ')
age = int(input('Enter age:'))

if marital_status == 'married':
    print('Driver is insured')
elif marital_status == 'unmarried' and sex == 'male' and age >=30:
    print('Driver is insured')
elif marital_status == 'unmarried' and sex == 'female' and age >=25:
    print('Driver is insured')
else:
    print('Driver is un insured')