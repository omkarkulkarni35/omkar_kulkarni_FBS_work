# Write a program to find maximum and minimum element in a list.

li = [10, 20, 30, 40, 50]

max = li[0]
for i in range(1,len(li)):
    if(li[i] > max):
        max = li[i]

print(f"Maximum number is : {max}")

min = li[0]
for i in range(0,len(li)):
    if (li[i] < min):
        min = li[i]

print(f"Minimum number is : {min}")