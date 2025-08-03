# Write a program to swap two numbers using third variable.

a = int(input("Enter a Number: "))
b = int(input("Enter a Number: "))

print(f"Displaying Number Before Swapping A={a},B={b}")

temp = a
a = b
b = temp

print(f"Displaying Number After Swapping A={a} ,B={b}")