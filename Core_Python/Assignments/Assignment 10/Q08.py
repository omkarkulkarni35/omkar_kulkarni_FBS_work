# Write a program to create a duplicate of an existing list. It should not point to same list.


original = [10, 20, 30, 40, 50]

duplicate = []

for i in range(len(original)):
    duplicate.append(original[i])

print("Original list:", original)
print("Duplicate list:", duplicate)
