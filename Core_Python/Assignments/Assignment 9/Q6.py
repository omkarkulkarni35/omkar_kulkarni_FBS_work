# Write a program to print Fibonacci series using recursion.

def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)

def print_fibonacci_series(count):
    print("Fibonacci series:")
    for i in range(count):
        print(fibonacci(i), end=' ')

num = int(input("Enter how many terms to print: "))
print_fibonacci_series(num)