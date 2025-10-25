# Python Program to Count the Frequency of Words Appearing in a String Using a Dictionary

text = input("Enter a string: ")

words = text.split()

word_freq = {}

for word in words:
    if word in word_freq:
        word_freq[word] += 1
    else:
        word_freq[word] = 1

print("Word Frequency:")
for word, freq in word_freq.items():
    print(f"{word}: {freq}")