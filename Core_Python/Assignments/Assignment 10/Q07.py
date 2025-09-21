# Write a program to create a new list from existing list which contains cube of each number of list.

original = [2, 3, 4, 5, 6]

cubes = []

for i in range(len(original)):
    cube = original[i] * original[i] * original[i]
    cubes.append(cube)

print("List of cubes:", cubes)
