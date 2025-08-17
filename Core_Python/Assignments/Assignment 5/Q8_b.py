n = int(input("Enter N for exponential sum: "))
exp_sum = 0
for i in range(1, n + 1):
    exp_sum += n ** i

print(f"Sum of powers from N¹ to Nⁿ is: {exp_sum}")