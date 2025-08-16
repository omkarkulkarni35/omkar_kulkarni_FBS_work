n = int(input("Enter the number: "))

a = 0
b = 1

for i in range(n):
    c = a + b   # sum of previous two
    a = b       # move forward
    b = c       # update b
    print(f"Fibonacci Series: ",a, end=" " )

