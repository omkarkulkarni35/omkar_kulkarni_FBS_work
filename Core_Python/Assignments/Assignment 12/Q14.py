# # Python Program to count the occurrences of ach word in a string.

text = input("Enter a string: ")

words = text.split()

word_count = {}

for word in words:
    if word in word_count:
        word_count[word] += 1
    else:
        word_count[word] = 1

print("Word occurrences:")
for word, count in word_count.items():
    print(f"{word}: {count}")