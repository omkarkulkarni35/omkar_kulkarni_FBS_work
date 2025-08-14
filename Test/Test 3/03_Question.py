n = int(input("Enter number of employees: "))
total_all_emp = 0

for i in range(1, n + 1):
    basic = float(input(f"Enter basic salary of employee {i}: "))

    if basic < 20000:
        da = basic * 0.10
        ta = basic * 0.12
        hra = basic * 0.15
    else:
        da = basic * 0.15
        ta = basic * 0.18
        hra = basic * 0.20

    total_salary = basic + da + ta + hra
    total_all_emp += total_salary
    print(f"Total salary of employee {i} = {total_salary}")

print(f"Total salary of all employees = {total_all_emp}")
