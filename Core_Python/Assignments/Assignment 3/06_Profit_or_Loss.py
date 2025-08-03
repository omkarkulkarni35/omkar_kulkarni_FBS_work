# Write a program to calculate profit or loss.

cost_price = float(input("Enter a Cost Price: "))
selling_price = float(input("Enter a Selling Price: "))

if(selling_price > cost_price):
    profit = selling_price - cost_price
    print(f"Profit = {profit}")

elif(selling_price < cost_price):
    loss = cost_price - selling_price
    print(f"Loss = {loss}")

else:
    print("No Profit No Loss")