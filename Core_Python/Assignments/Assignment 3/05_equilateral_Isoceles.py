# Write a program to check whether the triangle is equilateral, isosceles or scalene triangle.

a = int(input("Enter side 1: "))
b = int(input("Enter side 2: "))
c = int(input("Enter side 3: "))

if a == b and b == c:
    print("It is Eqilateral Triangle")

elif a == b or b == c or a == c:
    print("It is Isoceles Triangle")

else:
    print("It is Scalene Triangle")