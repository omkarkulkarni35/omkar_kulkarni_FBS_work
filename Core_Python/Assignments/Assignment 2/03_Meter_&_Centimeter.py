# Program to convert distance from feet and inches to meters and centimeters


feet = int(input("Enter distance in feet: "))
inches = int(input("Enter additional inches: "))


total_inches = (feet * 12) + inches

# 1 inch = 2.54 cm
total_cm = total_inches * 2.54


meters = int(total_cm // 100)
centimeters = total_cm % 100

# Displaying the result
print(f"{feet} feet and {inches} inches is equal to {meters} meters and {centimeters:.2f} centimeters")