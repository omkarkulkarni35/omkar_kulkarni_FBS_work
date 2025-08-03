# Write a program to check if user has entered correct userid and password.

user_id = str(input("Enter a USER_ID: "))
password = int(input("Enter a PASSWORD: "))

uid = "admin"
pwd = 1234

if user_id == uid and password == pwd:
    print("Login Sucessful")

else:
    print("Incorrect UserID or Password")