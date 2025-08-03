# WAP to calculate selling price of book based on cost price and discount.

cost_price = float(input("Enter the Cost Price of Book: "))

discount = float(input("Enter the discount in percentage: "))

discount_amt = (discount/100) * cost_price

selling_price = cost_price - discount_amt

print(f"The Selling Price of Book is {selling_price}")