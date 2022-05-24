
#Write a program to find the sum of ’n’ distinct numbers

n = (int(input("Enter distinct number till you want the sum: ")))
i = 1
s = 0
while i <= n:
    s+= i 
    i+= 1
print(f'sum of n distincts numbers is : {s}     ')
 