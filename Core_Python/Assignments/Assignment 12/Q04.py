# Python Program to Form a New String where the First Character and the Last Character have been Exchanged

text = input("Enter a string: ")

if len(text) < 2:
    print("String is too short to swap.")
else:
    first = text[0]
    last = text[-1]
    middle = text[1:-1]
    new_text = last + middle + first
    print("Modified string:", new_text)