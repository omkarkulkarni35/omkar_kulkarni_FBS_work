# Python Program to count number of lowercase characters in a string.

string = input("Enter a string: ")

count = 0

for char in string:
    if char.islower():
        count += 1

print(f"Count of Lowercase Character is: {count}")