# WAP to check User ID and Password with 3 attempts

correct_userid = "admin"
correct_password = "12345"

for attempt in range(1, 4):
    userid = input("Enter User ID: ")
    password = input("Enter Password: ")

    if userid == correct_userid and password == correct_password:
        print("Login Successful")
        break
    else:
        print(f"Incorrect credentials! Attempts left: {3 - attempt}")

else:
    print("Too many failed attempts. Program terminated.")
