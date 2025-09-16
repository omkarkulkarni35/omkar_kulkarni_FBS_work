# Write a program to check whether a number is prime or not using recursion.

def is_prime_recursive(n, divisor=2):
    if n <= 1:
        return False
    if divisor > n // 2:
        return True
    if n % divisor == 0:
        return False
    return is_prime_recursive(n, divisor + 1)

num = int(input("Enter a number: "))
if is_prime_recursive(num):
    print(f"{num} is a Prime number.")
else:
    print(f"{num} is NOT a Prime number.")