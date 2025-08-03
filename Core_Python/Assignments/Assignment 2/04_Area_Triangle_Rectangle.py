# WAP to calculate area of triangle and rectangle

base = float(input("Enter the Base of Triangle: "))
height = float(input("Enter the Height of Triangle: "))
length = float(input("Enter the Length of Rectangle: "))
width = float(input("Enter the Width of Rectangle: "))

area_triangle = (1/2) *base * height
area_rectangle = length * width

print(f"Area of Triangle is {area_triangle}")
print(f"Area of Rectangle is {area_rectangle}")