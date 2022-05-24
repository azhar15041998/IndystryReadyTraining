#50. Write a program to find the sum of even ‘n’ natural numbers.

n = (int(input("Enter distinct number till you want the sum: ")))
i = 0
s = 0
while i <= n:
    s+= i 
    i+= 2
print(f'sum of even natural numbers is : {s} ')
 