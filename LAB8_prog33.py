'''33. Write a program to calculate the monthly income of a person using the
following commission schedule:
Page 3 of 13
Monthly sales income
>= Rs.50,000 Rs.375 + 16% sales.
>= Rs.50,000 but >=Rs.40,000 Rs. 350+14% sales.
<= Rs.40,000 but >=Rs.30,000 Rs. 325+12% sales.
<= Rs.30,000 but >=Rs.20,000 Rs. 300+9% sales.
<= Rs.20,000 but >=Rs.10,000 Rs. 250+5% sales.
<= Rs.10,000 Rs. 200+3% sales.'''

income = float(input('Enter monthly income: '))
#after reading income we will apply below conditions for the commision 

if income >= 50000:
    print('The income after adding commision is :', income + 375 + ((16/100)*income))

elif income >= 50000 and income >= 40000:
    print('The income after adding commision is: ',income + 350 + ((14/100)*income))

elif income <= 40000 and income >= 30000:
    print('The income after adding commision is: ',income + 325 + ((12/100)*income))

elif income >= 30000 and income >= 20000:
    print('The income after adding commision is: ',income + 300 + ((9/100)*income))

elif income >= 30000 and income >= 20000:
    print('The income after adding commision is: ',income + 250 + ((9/100)*income))
    
elif income <= 10000:
        print('The income after adding commision is: ',income + 250 + ((3/100)*income))
else:
    print("")