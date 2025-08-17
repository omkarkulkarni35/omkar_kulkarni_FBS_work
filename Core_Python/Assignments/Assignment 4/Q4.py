n = int(input("Enter the Number: "))
i = 1
fact = 1

while(i <= n):
    fact *= i
    i = i + 1

print(f"The Factorial of {n} is {fact}")
