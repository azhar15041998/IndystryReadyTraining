#1. Write a function to return the given number is prime or not ? input --> number , output --> True/False


def  primea(n):
  for i in range(2,n): 
    if (n%i) == 0:
      return False
  return True
n = int(input("Enter the number: "))
primea(n)