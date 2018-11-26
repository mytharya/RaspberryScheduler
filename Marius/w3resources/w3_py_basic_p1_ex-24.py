# w3resources-24
# Write a Python program to test whether a passed letter is a vowel or not.

def ask4input():
    return str(input("Input one or more letters: "))

def check_if_input_is_alphabetic():
    if a4i.isalpha() == True:
        return True
    else:
        return False

def check4vowels():
    vowels = 0
    for char in a4i:
        if char in "aeiouAEIOU":
            vowels += 1
    return vowels

def respons3():
    if vowels_found < 2:
        print("Your input has {} vowel".format(vowels_found))
    else:
        print("Your input has {} vowels".format(vowels_found))

a4i = ask4input()
# print (a4i)
# check_if_input_is_alphabetic()
# 
while check_if_input_is_alphabetic() == False:
    a4i = ask4input()
# 
vowels_found = check4vowels()
# print(vowels_found)
# 
respons3()


# while a4i != None:6