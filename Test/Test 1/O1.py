# 1. Write a program to find the area and perimeter of following figure (Accept the
# length, breadth and radius from user:


length = float(input("Enter the Length: "))
breadth = float(input("Enter the Breadth: "))
radius = float(input("Enter the radius: "))

rectangle_area = length * breadth
rectangle_perimeter = 2 * (length * breadth)

circle_area = 3.14 * radius * radius
circle_circumference = 2 * 3.1416 * radius

print(f"Rectangle Area = {rectangle_area}")
print(f"Rectangle Perimeter = {rectangle_perimeter}")
print(f"Circle_Area = {circle_area}")
print(f"Circle Circumference = {circle_circumference}")