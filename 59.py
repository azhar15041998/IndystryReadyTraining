#Write a program to find the given number is prime or not.

for n in range(500,601):
    rt = int(n**0.5)
    for i in range(2,rt+1):
         if n%i==0:
            break
    else:
            print()
            print(n ,end='')

print( )
print( )


