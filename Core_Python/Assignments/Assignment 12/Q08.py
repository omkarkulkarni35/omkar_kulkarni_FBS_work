# Python Program to Remove the Characters of Odd Index Values in a String

string = input("Enter a String: ")

result = ""

for i in range(len(string)):
    if i % 2 == 0:
        result += string[i]

print(f"New String is: {result}")