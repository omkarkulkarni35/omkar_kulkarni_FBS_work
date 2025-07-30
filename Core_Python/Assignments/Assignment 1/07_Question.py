# Program to Find the Roots of a Quadratic Equation

a = float(input("Enter the number 1: "))
b = float(input("Enter the number 2: "))
c = float(input("Enter the number 3: "))

sqrt = ((b**2) - (4*a*c))**0.5

result1 = (-b+sqrt)/2*a
result2 = (-b-sqrt)/2*a

print(f"Roots of Quadratic equation is {result1}")
print(f"Roots of Quadratic equation is {result2}")