def area_of_circle(radius):
    pi = 3.14
    return pi * radius * radius

r = float(input("Enter radius of circle: "))
area = area_of_circle(r)
print("Area of circle =", area)
