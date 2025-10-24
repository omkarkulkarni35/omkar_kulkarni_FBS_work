# Python Program to Calculate the Length of a String Without Using a Library Function

string = input("Enter a String: ")

count = 0

for char in string:
    count += 1


print(f"The Lenth of String is: {count}")