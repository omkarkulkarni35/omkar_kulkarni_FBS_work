# Write a Python program to find elements in a given set that are not in
# another set.

set1 = {1, 2, 3, 4, 5}
set2 = {3, 4, 5}

res = set1.difference(set2)

print(f"Elememts in Set1 but not in Set2 is: {res}")
