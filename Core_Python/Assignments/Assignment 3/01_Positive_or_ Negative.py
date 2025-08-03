# Write a program to check if the given number is positive or negative.

num  = int(input("Enter the number: "))

if(num > 0):
    print(f"{num} is a positive number")

elif(num < 0):
    print(f"{num} it is a negative number")

else:
    print("The Number is Zero")