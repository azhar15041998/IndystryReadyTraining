#48. Write a program to find the sum of ‘n’ natural numbers.

n = int(input("Enter a value: "))
sum = 0

for i in range(1, n+1):
    print(i)
    sum += i

print(f"Sum of first {n} natural numbers: {sum}" )
 