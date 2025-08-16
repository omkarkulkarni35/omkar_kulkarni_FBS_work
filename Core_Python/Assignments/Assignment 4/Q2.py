n = int(input("Enter a range of number to print Odd Number: "))

for i in range(1, n+1):
    if(i % 2 != 0):
        print(i, end=" ")
