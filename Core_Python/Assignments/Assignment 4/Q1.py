n = int(input("Enter a number range to print Even Number: "))

for i in range(1, n+1):
    if(i % 2 == 0):
        print(i, end=" ")
