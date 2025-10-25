# Python Program to Multiply All the Items in a Dictionary

my_dict = {'a': 2, 'b': 3, 'c': 4}

mul = 1

for key in my_dict:
    mul *= my_dict[key]

print("Sum of all values:", mul)