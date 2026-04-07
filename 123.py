vowels = 0
word = "shatha"
for char in word :
    if char.lower()in "aeiou":
        vowels = vowels + 1
print(vowels)