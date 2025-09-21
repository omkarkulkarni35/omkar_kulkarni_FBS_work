# Write a program to remove all occurrences of a given element in the list.

original = [5, 3, 7, 3, 9, 3, 2]

target = int(input("Enter the element to remove: "))

filtered = []

for i in range(len(original)):
    if original[i] != target:
        filtered.append(original[i])

print("List after removing", target, ":", filtered)