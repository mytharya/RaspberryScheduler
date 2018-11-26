# w3resources-23
# Write a Python program to get the n (non-negative integer) copies of the first 2 characters of a given string. Return the n copies of the whole string if the length is less than 2.

# def ask4input():
#     while True:
#         try:
#             global str1ng
#             str1ng = str(input("Please input a string: "))
#             if str1ng.isalpha() == True:
#                 break
#             # break
#         except:
#             print("Thats a no no, mister!")
#     while True:
#         try:
#             global int3ger
#             int3ger = int(input("How many times to repeat the first two characters of your string? "))
#             if int3ger >= 0:
#                 break
#         except:
#             print("Thats a no no, mister!")

# ask4input()
# # print("smtg")

# def do_the_thingy():
#     if len(str1ng) < 2:
#         print((str1ng + ".")*int3ger)
#     else:
#         print((str1ng[:2] + ".")*int3ger)

# do_the_thingy()

# -------------------------------------------------------------

def check_if_alpha(strXXng):
    if strXXng.isalpha() == True:
        return True
    else:
        return False

def check_if_num(num3ric):
    if num3ric.isdigit() == True:
        return True
    else:
        return False


def ask4input_alpha():
    # print description
    # request input
    # check if value is non alfa by calling check_if_alphach whcich reurns True=contains only letters, False=otherwise
    # if values is fine, return the value
    str1ng = str(input("Please input a string: "))
    if check_if_alpha(str1ng) == True:
        return str1ng

def ask4input_num():
    num3ric = str(input("Please input a number: "))
    if check_if_num(num3ric) == True:
        return int(num3ric)

# ask4input_alpha()
# ask4input_num()

a4a = ask4input_alpha()
a4n = ask4input_num()

while a4a == None:
    a4a = ask4input_alpha()

while a4n == None:
    a4n = ask4input_num()

print(type(a4a))
print(type(a4n))
print((a4a[:2]+".")*a4n)

# print(a4a)
# print(a4n)