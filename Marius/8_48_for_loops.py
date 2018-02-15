#8_48 for loops

for number in range(1,10):
    print(number)

# vowels counter

vowels = 0
consonants = 0
letters = 0
word = []

print("input word to count vowels and consonants. \n")
word = input ("Input word:").strip().lower()
print()

for letter in word:
    letters = word.count("") - 1
    if letter.lower() in "aeiou":
        vowels = vowels + 1
    elif letter == "":
        pass
    else:
        consonants = consonants + 1

print("There are {} vowel(s). \n".format(vowels))
print("There are {} consonant(s). \n".format(consonants))
print("There are {} letter(s) in {} \n".format(letters,word))

