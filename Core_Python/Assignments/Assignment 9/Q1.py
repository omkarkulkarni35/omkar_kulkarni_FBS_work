def sum_factorials(n):
    if n == 0:
        return 0
    return factorial(n) + sum_factorials(n - 1)

def factorial(k):
    if k == 0 or k == 1:
        return 1
    return k * factorial(k - 1)

n = int(input("Enter n: "))
print("Sum of factorials:", sum_factorials(n))