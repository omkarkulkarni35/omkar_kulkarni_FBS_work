# Write a program to reverse a number using recursion.

def reverse_number(n, rev=0):
    if n == 0:
        return rev
    digit = n % 10
    rev = rev * 10 + digit
    return reverse_number(n // 10, rev)

num = int(input("Enter a number: "))
reversed_num = reverse_number(num)
print(f"Reversed number: {reversed_num}")