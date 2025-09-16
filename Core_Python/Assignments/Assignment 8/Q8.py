# 8. Write a program find reverse of a number

def reverse_number(n):
    reverse = 0
    while n > 0:
        digit = n % 10
        reverse = reverse * 10 + digit
        n = n // 10
    return reverse

num = int(input("Enter a number: "))
print("Reversed number:", reverse_number(num))