# Python Program to Remove the nth Index Character from a Non-Empty String

text = input("Enter a string: ")
n = int(input("Enter the index to remove: "))

if n < 0 or n >= len(text):
    print("Invalid index!")
else:
    Newtext = text[:n] + text[n+1:]
    print("Modified string:", Newtext)