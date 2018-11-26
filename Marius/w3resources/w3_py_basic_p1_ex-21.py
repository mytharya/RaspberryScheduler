# w3resources-21
# Write a Python program to find whether a given number (accept from the user) is even or odd, print out an appropriate message to the user.

def ask4input():
    while True:
        try:
            global valu3
            valu3 = input("Input smtg to evaluate it as even or odd: ")
            break
        except:
            print("naah! again!")

ask4input()
# print(valu3)

def evaluation():
    if len(valu3) % 2 == 0:
        print("Your number is EVEN")
    else:
        print("Your number is ODD")

evaluation()
