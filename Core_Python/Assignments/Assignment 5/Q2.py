num_students = int(input("Enter number of students: "))
total_percentage = 0

for i in range(1, num_students + 1):
    print(f"\nEnter marks of 5 subjects for Student {i}:")
    total_marks = 0
    for j in range(1, 6):
        marks = int(input(f" Subject {j}: "))
        total_marks += marks
    
    percentage = (total_marks / 500) * 100
    print(f" Percentage of Student {i}: {percentage}%")
    total_percentage += percentage

average_percentage = total_percentage / num_students
print(f"\nAverage Percentage of all students: {average_percentage}%")
