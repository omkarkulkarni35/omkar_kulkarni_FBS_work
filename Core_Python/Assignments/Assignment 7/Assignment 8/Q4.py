# Function to calculate sum of odd numbers
def sum_of_odds(n):
    total = 0
    for i in range(1, n+1):
        if i % 2 != 0:
            total += i
    return total

n = int(input("Enter a number: "))

print("Sum of odd numbers from 1 to", n, "is:", sum_of_odds(n))
