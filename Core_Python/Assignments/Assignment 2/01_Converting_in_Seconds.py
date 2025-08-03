# Convert the time entered in hh,min and sec into seconds.

hours = int(input("Enter a Hours: "))
minutes = int(input("Enter a Minutes: "))
seconds = int(input("Enter a Seconds: "))

total_seconds = (hours * 36000) + (minutes * 60) + seconds

print(f"The Total Seconds = {total_seconds}")