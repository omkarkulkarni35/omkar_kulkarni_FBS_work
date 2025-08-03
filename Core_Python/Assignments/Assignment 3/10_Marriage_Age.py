# Write a program to check if person is eligible to marry or not (male age >=21 and female age>=18)

name = str(input("Enter a Name: "))
gender = str(input("Enter a Gender (M/F): "))
age = int(input("Enter a Age: "))

if(gender == "M" and age >= 21) or (gender == "F" and age >= 18):
    print("You are Eligible for Marriage")

else:
    print("You are not Eligible to Marriage")