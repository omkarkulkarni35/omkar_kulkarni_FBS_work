n = int(input("Enter number of terms for geometric series: "))
geo_sum = 0
term = 1

for i in range(n):
    geo_sum += term
    term *= 2

print(f"Sum of geometric series with ratio 2 for {n} terms is: {geo_sum}")