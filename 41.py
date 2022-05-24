#Write a program to numbers divisible by 7 and multiple of 5, between 1 and 100.

#here we can user for loop to print the range which are div by 7 and mul of 5
for x in range(1,100):
    if x %7 ==0 and x%5==0: #since we need both conditions to be true we use and 
        print(x)
        