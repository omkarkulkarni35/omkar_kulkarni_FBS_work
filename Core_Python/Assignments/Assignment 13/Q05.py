# Python Program to Sum All the Items in a Dictionary

my_dict = {'a': 10, 'b': 20, 'c': 30}

total = 0

for key in my_dict:
    total += my_dict[key]

print("Sum of all values:", total)