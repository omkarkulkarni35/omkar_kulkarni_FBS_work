# Write a program to accept distance in km and convert it into meters and
# centimeters both.


kilometers = float(input("Enter distance in kilometers: "))

meters = kilometers * 1000
centimeters = kilometers * 100000

print(f"Distance in Meters: {meters}")
print(f"Distance in Centimeters: {centimeters}")