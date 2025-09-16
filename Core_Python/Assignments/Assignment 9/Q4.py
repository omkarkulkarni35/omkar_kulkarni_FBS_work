# Write a program to find sum of n numbers using recursion.

def sum_n(n):
    if n == 0:
        return 0
    return n + sum_n(n - 1)

num = int(input("Enter a number: "))
total = sum_n(num)
print(f"Sum of first {num} natural numbers is: {total}")