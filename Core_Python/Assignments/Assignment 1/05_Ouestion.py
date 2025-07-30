# Program to calculate Compound Interest


P = float(input("Enter the Principal amount (P): "))
T = float(input("Enter the Time in years (T): "))
R = float(input("Enter the Rate of Interest per year (R): "))


A = P * (1 + R / 100) ** T
CI = A - P    


print(f"Compound Interest is: {CI}")