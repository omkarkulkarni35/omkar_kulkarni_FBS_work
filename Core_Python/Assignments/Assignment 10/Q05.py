# Accept a number from user and check if this element is present in the list or not. Also tell how many times it is present in the list.

numbers = [4, 7, 2, 7, 9, 7, 1, 5]

target = int(input("Enter a number to search: "))

count = 0


for i in range(len(numbers)):
    if numbers[i] == target:
        count = count + 1

if count > 0:
    print(target, "is present in the list.")
    print("It appears", count, "times.")
else:
    print(target, "is not present in the list.")