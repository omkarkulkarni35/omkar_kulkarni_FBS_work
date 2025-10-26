# Write a Python program that finds all pairs of elements in a list whose
# sum is equal to a given value.

numbers = [1, 4, 6, 2, 3, 5, 7]
target = int(input("Enter the target sum: "))

pairs = []

for i in range(len(numbers)):
    for j in range(i + 1, len(numbers)):
        if numbers[i] + numbers[j] == target:
            pairs.append((numbers[i], numbers[j]))

print(f"Pairs with sum {target}:")
for p in pairs:
    print(p)