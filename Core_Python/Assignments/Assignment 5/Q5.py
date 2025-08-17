amt = int(input("Enter amount to calculate min: "))
current = [2000, 500, 200, 100, 50, 20, 10]
total_notes = 0

for note in current:
    count = amt // note
    total_notes += count
    amt = amt % note

print(f"Total no. of notes {total_notes}")