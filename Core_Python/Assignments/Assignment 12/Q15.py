# Python Program to find larger string without using built-in functions.

string1 = input("Enter a First String: ")
string2 = input("Enter a Second String: ")

count1 = 0
for char1 in string1:
    count1 += 1

count2 = 0
for char2 in string2:
    count2 += 1

if count1 > count2:
    print(f"The Larger String is {string1}")

elif count2 > count1:
    print(f"The Larger String is: {string2}")

else:
    print("Both String are Same.")