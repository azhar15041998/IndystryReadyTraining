'''14. The temperature of the city is input through the keyboard in Fahrenheit. Write
a program to convert into Celsius'''
Fahrenheit  = float(input('Enter Fahrenheit  Value : '))

#calculates Fahrehheit to celcius 
Celcius = (Fahrenheit - 32) *(5 / 9)
print(f'The Celcius of the entered Fahrenheit is : {Celcius}')