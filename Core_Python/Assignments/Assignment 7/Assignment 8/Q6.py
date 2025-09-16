# Write a program to find print the following Fibonacci series using functions:
# 1 1 2 3 5 8 n terms


def print_fibonacci(n):
    a = 1
    b = 1
    print(a, b, end=' ')
    for _ in range(n - 2):
        c = a + b
        print(c, end=' ')
        a = b
        b = c

n = int(input("Enter number of terms: "))
print("Fibonacci series:")
print_fibonacci(n)