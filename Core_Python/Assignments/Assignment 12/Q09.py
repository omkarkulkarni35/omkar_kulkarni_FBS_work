# Python Program to Calculate the Number of Words and the Number of Characters Present in a String

string = input("Enter a String: ")

char_count = 0

for char in string:
    char_count += 1

words = string.split()
word_count = 0
for word in words:
    word_count += 1

print(f"Char Count is: {char_count}")
print(f"Words Count is: {word_count}")