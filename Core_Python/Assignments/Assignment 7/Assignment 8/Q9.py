# Write a program to check if entered year is a leap year or not.

def reverse_number(n):
    reverse = 0
    temp = n
    while temp > 0:
        digit = temp % 10
        reverse = reverse * 10 + digit
        temp = temp // 10
    return reverse


def is_palindrome(n):
    return n == reverse_number(n)


num = int(input("Enter a number: "))
if is_palindrome(num):
    print("It is a palindrome.")
else:
    print("It is not a palindrome.")