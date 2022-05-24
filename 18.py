'''18. The distance between two cities in Km. is input through the keyboard. Write a
program to convert and print the result in meters and centimetres.'''

Kilometer = float(input("Enter kilometer : ")) #it takes kilometer as input
Meter = Kilometer * 1000 #1 km is equal to 1000 meteres
Centi_meter = Kilometer * 100000 #1 km is equal to 10000 ccenti meteres
print(f'kilometers in Meter is : {Meter} \nKilometers in Centimeter is : {Centi_meter}')

