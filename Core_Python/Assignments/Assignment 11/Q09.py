# Write a program to create three lists of numbers, their squares and cubes

start = 1
end = 10

numbers = []
squares = []
cubes = []

for num in range(start, end + 1):
    numbers.append(num)
    squares.append(num ** 2)
    cubes.append(num ** 3)

print("Numbers :", numbers)
print("Squares :", squares)
print("Cubes   :", cubes)