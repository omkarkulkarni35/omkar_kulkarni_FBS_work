# Write a program to print list after removing even numbers.

original = [12, 7, 9, 4, 6, 11, 8, 3]

filtered = []

for i in range(len(original)):
    if original[i] % 2 != 0:
        filtered.append(original[i])

print("List after removing even numbers:", filtered)