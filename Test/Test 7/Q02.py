strings = input("Enter a list of strings separated by spaces: ").split()

uppercase_strings = [s.upper() for s in strings]

print("Uppercase versions of the strings are:", uppercase_strings)
