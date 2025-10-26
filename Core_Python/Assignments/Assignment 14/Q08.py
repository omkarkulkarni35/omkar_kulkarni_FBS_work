# Write a Python program to find all the anagrams and group them
# together from a given list of strings.
# Sample list of strings

words = ["bat", "tab", "tap", "pat", "top", "pot", "listen", "silent", "enlist"]

anagram_groups = {}

for word in words:
    signature = ''.join(sorted(word))
    
    if signature in anagram_groups:
        anagram_groups[signature].append(word)
    else:
        anagram_groups[signature] = [word]

print("Grouped Anagrams:")
for group in anagram_groups.values():
    print(group)
