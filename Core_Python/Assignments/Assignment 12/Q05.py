# Python Program to Count the Number of Vowels in a String

text = input("Enter the the String: ")

vowels = "aeiouAEIOU"

count = 0

for char in text:
    if char in vowels:
        count += 1

print(f"Vowel count in string is: {count}")