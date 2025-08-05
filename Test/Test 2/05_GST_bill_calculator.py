
product1 = float(input("Enter price of product 1: "))
product2 = float(input("Enter price of product 2: "))
product3 = float(input("Enter price of product 3: "))
product4 = float(input("Enter price of product 4: "))
product5 = float(input("Enter price of product 5: "))


total_price = product1 + product2 + product3 + product4 + product5


gst = (18 / 100) * total_price


total_bill = total_price + gst


print(f"Total price without GST: ₹ {total_price}")
print(f"GST (18%): ₹{gst}")
print(f"Total bill after adding GST: ₹{total_bill}")
