# Python Program to Put Even and Odd elements of a List into two Different Lists

numbers = [12, 7, 9, 14, 5, 8, 3, 10]

even_list = []
odd_list = []

for num in numbers:
    if num % 2 == 0:
        even_list.append(num)
    else:
        odd_list.append(num)

print("Even numbers:", even_list)
print("Odd numbers:", odd_list)