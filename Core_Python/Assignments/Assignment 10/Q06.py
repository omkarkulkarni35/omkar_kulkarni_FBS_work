# Write a program to remove duplicates from the list.

original = [4, 7, 2, 4, 9, 7, 2, 1]

unique = []

for i in range(len(original)):
    found = False

    for j in range(len(unique)):
        if original[i] == unique[j]:
            found = True
            break

    if not found:
        unique.append(original[i])

print("List after removing duplicates:", unique)