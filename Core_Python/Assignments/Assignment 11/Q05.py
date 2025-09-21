# Python Program to Sort a List According to the Length of the Elements within the list.

words = ["apple", "banana", "kiwi", "grape", "watermelon", "fig"]

def get_length(item):
    return len(item)

sorted_words = sorted(words, key=get_length)


print("Sorted by Length:", sorted_words)