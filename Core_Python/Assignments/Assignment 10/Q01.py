# Write a program to find sum of all elements of list

numbers = [5, 10, 15, 20, 25]

total = 0

for i in range(len(numbers)):
    total = total + numbers[i]

print("Sum of all elements:", total)