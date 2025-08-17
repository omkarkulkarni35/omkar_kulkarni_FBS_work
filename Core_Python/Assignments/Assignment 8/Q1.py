# Function to calculate area of rectangle
def area_rectangle(length, width):
    return length * width

# Main program
l = float(input("Enter the length of rectangle: "))
w = float(input("Enter the width of rectangle: "))

area = area_rectangle(l, w)
print("The area of the rectangle is:", area)
