# Accept age of five people and also per person ticket amount and then calculate total amount to ticket to travel for all of them based on following condition :
# a. Children below 12 = 30% discount
# b. Senior citizen (above 59) = 50% discount
# c. Others need to pay full.

ticket_price = int(input("Enter the Ticket Fare: "))
total_amt = 0

for i in range(1, 6):
    age = int(input(f"Enter the age of Person {i}: "))
    
    if age < 12:
        amt = ticket_price * 0.70
    elif age > 59:
        amt = ticket_price * 0.50
    else:
        amt = ticket_price
    
    total_amt += amt
    print(f"Amount for Person {i}: {amt}")

print(f"\nTotal Amount for All Persons: {total_amt}")