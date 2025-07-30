# Write a program to calculate the percentage of student based on marks of any 5 subjects.

m1 = int(input("Enter marks of Marathi: "))
m2 = int(input("Enter marks of Hindi : "))
m3 = int(input("Enter marks of English 3: "))
m4 = int(input("Enter marks of Science 4: "))
m5 = int(input("Enter marks of Maths 5: "))

total_marks = m1 + m2 + m3 + m4 + m5

percentage = (total_marks/500)*100

print(f"Percentage of given marks is: {percentage}%")