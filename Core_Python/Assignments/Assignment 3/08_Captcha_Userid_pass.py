import random

user_id = str(input("Enter a UserID: "))
password = int(input("Enter a Password: "))

uid = "admin"
pwd = 1234

if user_id == uid and password == pwd:
    captcha = random.randint(1111,9999)
    print(f"Captcha = {captcha}")

    user_input = int(input("Enter a above Captcha: "))

    if user_input == captcha:
        print("Login Sucessful")

    else:
        print("Captcha Verification Failed")

else:
    print("Incorrect UserId Or Password")