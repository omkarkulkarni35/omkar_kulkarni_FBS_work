# WAP to check if a given number is Perfect Number or not

num = int(input("Enter a number: "))
sum_of_divisors = 0


for i in range(1, num):
    if num % i == 0:
        sum_of_divisors += i


if sum_of_divisors == num:
    print(num, "is a Perfect Number")
else:
    print(num, "is NOT a Perfect Number")
