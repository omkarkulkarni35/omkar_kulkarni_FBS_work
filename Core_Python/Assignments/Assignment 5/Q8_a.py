n = int(input("Enter n for factorial sum: "))
fact_sum = 0
for i in range(1, n + 1):
    fact = 1
    for j in range(1, i + 1):
        fact *= j
    fact_sum += fact

print(f"Sum of factorials up to {n}! is: {fact_sum}")