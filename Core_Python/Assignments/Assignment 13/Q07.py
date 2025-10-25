# Python Program to Remove the Given Key from a Dictionary

my_dict = {'name':'Omkar','age':'23','city':'Pune'}

remove = input("Enter a Key to remove: ")

new_dict = {}

for key in my_dict:
    if key != remove:
        new_dict[key] = my_dict[key]

print(f"Old Dictionary: {my_dict}")
print(f"New Dictionary: {new_dict}")