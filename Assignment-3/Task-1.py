#Task 1: Calculate Factorial Using a Function

def factorial(num):
    if num<2:
        return 1
    else:
        return num * factorial(num-1)

a=int(input("Enter the number to find factorial: "))
result= factorial(a)
print("The Factorial of Number ",a," is: ", result)
