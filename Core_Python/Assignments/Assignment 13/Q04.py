# Python Program to Generate a Dictionary that Contains Numbers (between 1
# and n) in the Form (x,x*x).

n = int(input("Enter the n mumber: "))

squre_dict = {}

for x in range(1,n+1):
    squre_dict[x] = x * x

print(f"Generated Dixtionary is: {squre_dict}")