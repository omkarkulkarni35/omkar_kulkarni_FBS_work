# Write a program to input all sides of a triangle and check whether triangle is valid or not.

a = int(input("Enter the side1: "))
b = int(input("Enter the side2: "))
c = int(input("Enter the side3: "))

sum_of_all_sides = a + b + c



if(sum_of_all_sides==180) and (a+b)>c and (b+c)>a and (a+c)>b:
    print("It is Valid Triangle")

else:
    print("It is Not Valid Triangle")