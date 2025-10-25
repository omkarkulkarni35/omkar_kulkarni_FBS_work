# Python Program to Check if a Given Key Exists in a Dictionary or Not

dict = {'name':'omkar','Age':'23','city':'pune'}

check = input("Enter a Key to check: ")

found = False
for key in dict:
    if key == check:
        found = True
        break

if found:
    print("Given key is exist in Dictionary.")

else:
    print("Given key is not exist in Dictionary")