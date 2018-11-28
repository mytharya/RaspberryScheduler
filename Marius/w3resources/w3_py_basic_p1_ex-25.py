# w3resources-25
# Write a Python program to check whether a specified value is contained in a group of values.
# Ex:
# 3 -> [1, 5, 8, 3] : True
# -1 -> [1, 5, 8, 3] : False

def ask4input(text):
    return input(text)

def minimum_lenght(value):
    while len(value) > 1:
        return True
    else:
        return False

def check_if_isdigit(value):
    if value.isdigit() == True:
        return True
    else:
        return False

def check_if_has_minimum_lenght(value):
    while len(value) > 1:
        return True
    else:
        return False

times = ask4input("How many numbers you wish to introduce in order me to compare it with the last number: ")

while check_if_isdigit(times) == False:
    times = ask4input("How many numbers you wish to introduce in order me to compare it with the last number: ")
else:
    for item in range(1, (int(times)+1)):
        print(item)
        a4i_+item = ask4input("I need a number: ")
        while check_if_isdigit(a4i_item) == False or check_if_has_minimum_lenght(a4i_item) == False:
            print("False?, not good :(")
            a4i_item = ask4input("I need a JUST and/or MORE numbers: ")
        else:
            continue

print(a4i)