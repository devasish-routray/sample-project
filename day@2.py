# This program calculates the factorial of a number entered by the user.

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)
num = int(input("Enter a number: "))
print("Factorial of", num, "is", factorial(num))




 
 