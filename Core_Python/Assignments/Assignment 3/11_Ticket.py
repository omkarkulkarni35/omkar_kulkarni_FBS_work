# Accept age of five people and also per person ticket amount and then calculate total amount to ticket to travel for all of them based on following condition :
# a. Children below 12 = 30% discount
# b. Senior citizen (above 59) = 50% discount
# c. Others need to pay full.

total_amt = 0

ticket_price = int(input("Enter the Ticket Fare: "))

#for person 1
age1 = int(input("Enter the Age of Person 1: "))

if(age1 < 12):
    amt1 = ticket_price * 0.70

elif(age1 > 59):
    amt1 = ticket_price * 0.50

else:
    amt1 = ticket_price
total_amt = total_amt + amt1

print(f"Total Amount of Person 1: {amt1}")

#for person 2

age2 = int(input("Enter the age of Person 2: "))

if(age2 < 12):
    amt2 = ticket_price * 0.70

elif(age2 > 59):
    amt2 = ticket_price * 0.50

else:
    amt2 = ticket_price
total_amt = total_amt + amt2

print(f"The Total amount of Person 2: {amt2}")

#for person 3

age3 = int(input("Enter the age of Person 3: "))

if(age3 < 12):
    amt3 = ticket_price * 0.70

elif(age3 > 59):
    amt3 = ticket_price * 0.50

else:
    amt3 = ticket_price
total_amt = total_amt + amt3

print(f"The total amount of person 3 is: {amt3} ")

#for person 4

age4 = int(input("Enter the age of Prson 4:"))

if(age4 < 12):
    amt4 = ticket_price * 0.70

elif(age4 > 59):
    amt4 = ticket_price * 0.50

else:
    amt4 = ticket_price
total_amt = total_amt + amt4

#for person 5

age5 = int(input("Enter the age of Person 5: "))

if(age5 < 12):
    amt5 = ticket_price * 0.70

elif(age5 > 59):
    amt5 = ticket_price * 0.50

else:
    amt5 = ticket_price
total_amt = total_amt + amt5
print(f"The total amount of Person 5: {amt5}")

all_person_total = amt1 + amt2 + amt3 + amt4 + amt5

print(f"The Total Amount of All Person is: {all_person_total}")