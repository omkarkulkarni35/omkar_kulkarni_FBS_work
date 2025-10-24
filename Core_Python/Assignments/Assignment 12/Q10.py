# Python Program to Take in Two Strings and Display the Larger String without Using Built-in Functions

str1 = input("Enter a First String: ")
str2 = input("Enter a Second String: ")

count1 = 0
for char1 in str1:
    count1 += 1

count2 = 0
for char2 in str2:
    count2 += 1

if count1 > count2:
    print(f"Larger String is: {str1}")

elif count2 > count1:
    print(f"Larger String is: {str2}")

else:
    print("Both Strings are Same.")