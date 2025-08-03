# Write a program to input angles of a triangle and check whether triangle is valid or not.

angle1 = int(input("Enter a Angle1: "))
angle2 = int(input("Enter a Angle2: "))
angle3 = int(input("Enter a Angle3: "))

sum_angles = angle1 + angle2 + angle3

if(sum_angles==180 and angle1 > 0 and angle2 > 0 and angle3 > 0):
    print("It is Triangle")

else:
    print("It is not a Triangle")