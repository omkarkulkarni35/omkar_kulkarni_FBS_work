# Write a program to input any alphabet and check whether it is vowel or consonant.

alphabet = str(input("Enter a Alphabet: "))

vowel = "AEIOUaeiou"

if(alphabet==vowel):
    print(f"{alphabet} is a Vowel")

else:
    print(f"{alphabet} is a Consonant")