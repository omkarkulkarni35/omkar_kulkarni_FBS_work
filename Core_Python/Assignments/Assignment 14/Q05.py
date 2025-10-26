words = ["flower", "flow", "flight"]

min_length = min(len(word) for word in words)

prefix = ""

for i in range(min_length):
    chars_at_i = {word[i] for word in words}

    if len(chars_at_i) == 1:
        prefix += chars_at_i.pop()
    else:
        break

print("Longest common prefix:", prefix)