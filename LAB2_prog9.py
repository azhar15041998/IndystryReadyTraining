#9. Write a program to find your age in days.
from datetime import datetime, timedelta  #imports date packages
particular_date = datetime(1998, 4, 15)   #need to  pass year , month,day
new_date = datetime.today() - particular_date  #subtract entered date with current date  
print (new_date.days)  #print total days  ,since date.