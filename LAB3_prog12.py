#12. Write a program to convert the given seconds into hours – minutes – seconds. 
seconds = int(input('Enter Seconds : '))
minutes = seconds / 60  #calculates minutes
hours =  seconds / 3600 #calculates hours
print(f'The seconds into hour is : {hours}  \nThe seconds into minuts is  {minutes}')
