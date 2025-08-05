
height = float(input("Enter the height of the wall (in meters): "))
width = float(input("Enter the width of the wall (in meters): "))
cost_per_sq_meter = float(input("Enter the cost of painting per square meter: "))


area_one_wall = height * width

total_area = 4 * area_one_wall


total_cost = total_area * cost_per_sq_meter

print(f"Total cost of painting four walls is: ₹ {total_cost}")
