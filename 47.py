# 47. Write a program to find whether the given numbers existing in an array or not.


arr = input("enter array:")
print(arr)
num = input("enter num:")
print(num)
    
for num in arr:   #'in' is used to check weather element present in array or not
    print("yes")
    break
else:
    print("no")