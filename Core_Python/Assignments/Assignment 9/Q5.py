# Write a program to find factorial using recursion.

def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)

num = int(input("Enter a number: "))
result = factorial(num)
print(f"Factorial of {num} is: {result}")