# Write a program to swap two numbers without using third variable.

a = int(input("Enter first number (a): "))
b = int(input("Enter second number (b): "))

# Display before swapping
print("\nBefore Swapping:")
print("a =", a)
print("b =", b)


a = a + b
b = a - b
a = a - b


# Display after swapping
print("\nAfter Swapping:")
print("a =", a)
print("b =", b)
