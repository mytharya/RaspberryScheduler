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
    print(value)
    while value.isdigit() != True:
        value = ask4input("You got to input JUST numbers!: ")
        return value

def check_if_has_minimum_lenght(a4i):
    while minimum_lenght(a4i) != True:
        a4i = ask4input("You got to input MORE numbers!: ")
        return a4i

a4i = ask4input("I need a few numbers: ")

check_if_isdigit(a4i)

check_if_has_minimum_lenght(a4i)


print(a4i)







