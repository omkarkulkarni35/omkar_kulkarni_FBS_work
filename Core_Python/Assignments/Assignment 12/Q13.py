# Python Program to count number of digits and letters in a string.

string = input("Enter a String: ")

letter_count = 0
digit_count = 0

for char in string:
    if char.isalpha():
        letter_count += 1
    elif char.isdigit():
        digit_count += 1

print("Letter Count is",letter_count)
print("Digit Count is:",digit_count)