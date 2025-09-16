# Function to calculate sum of natural numbers: 1 + 2 + 3 + ... + n
def sum_of_natural_numbers(n):
    total = 0
    for i in range(1, n + 1):
        total += i
    return total

# Function to calculate factorial of a number
def factorial(num):
    result = 1
    for i in range(1, num + 1):
        result *= i
    return result

# Function to calculate sum of factorials: 1! + 2! + 3! + ... + n!
def sum_of_factorials(n):
    total = 0
    for i in range(1, n + 1):
        total += factorial(i)
    return total

# Function to calculate sum of self powers: 1^1 + 2^2 + 3^3 + ... + n^n
def sum_of_self_powers(n):
    total = 0
    for i in range(1, n + 1):
        total += i ** i
    return total


def main():
  
    n = int(input("Enter a positive integer (n): "))

 
    print("\nResults:")
    print("a. Sum of natural numbers:", sum_of_natural_numbers(n))
    print("b. Sum of factorials:", sum_of_factorials(n))
    print("c. Sum of self powers:", sum_of_self_powers(n))

main()