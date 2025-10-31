start = int(input("Enter the starting number: "))
end = int(input("Enter the ending number: "))

odd_numbers = [num for num in range(start, end + 1) if num % 2 != 0]

print("Odd numbers from", start, "to", end, "are:", odd_numbers)
