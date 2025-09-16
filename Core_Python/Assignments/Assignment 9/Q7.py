# Write a program to find sum of digits using recursion.

def sum_of_digits(n):
    if n == 0:
        return 0
    digit = n % 10
    return digit + sum_of_digits(n // 10)

num = int(input("Enter a number: "))
result = sum_of_digits(num)
print(f"Sum of digits of {num} is: {result}")