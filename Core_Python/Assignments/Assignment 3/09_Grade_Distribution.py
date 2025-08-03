# Input 5 subject marks from user and display grade(eg.First class,Second class ..)

sub1 = int(input("Enter the marks of Marathi: "))
sub2 = int(input("Enter the marks of Hindi: "))
sub3 = int(input("Enter the marks of English: "))
sub4 = int(input("Enter the marks of Science: "))
sub5 = int(input("Enter the marks of Maths: "))

total = sub1 + sub2 + sub3 + sub4 + sub5
percentage = total/5

if(percentage >= 75 ):
    print(f"{percentage}% Congratulation You are Pass With Distintion ")

elif(percentage >= 60):
    print(f"{percentage}% Congratulation You are Pass With First Class ")

elif(percentage >= 35):
    print(f"{percentage}% Congratulation You are Pass With Second Class ")

else:
    print("Sorry You are Failed")