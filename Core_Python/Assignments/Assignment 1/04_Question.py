# Write a program to enter P, T, R and calculate simple Interest.

P = float(input("Enter the Principal Amount (P): "))
T = float(input("Enter the Time in Years (T): "))
R = float(input("Enter the Rate of Interest (R): "))

SI = (P * T * R)/100

print(f"The Simple Interest is {SI}")