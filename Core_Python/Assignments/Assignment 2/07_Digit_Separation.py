# Find the sum of three-digit number.

num = int(input("Enter three digit number: "))
temp = num

digit1 = temp % 10
temp = temp // 10

digit2 = temp % 10
temp = temp // 10

digit3 = temp % 10
temp = temp // 10

print(f"Digit1:{digit1}, Digit2:{digit2}, Digit3:{digit3}")