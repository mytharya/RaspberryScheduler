# w3resources-25
# Write a Python program to check whether a specified value is contained in a group of values.
# Ex:
# 3 -> [1, 5, 8, 3] : True
# -1 -> [1, 5, 8, 3] : False

def ask4input(text):
    return input(text)

def minimum_lenght(value):
    if value == None:
        return False
    elif len(value) > 1:
        return True
    else:
        return False

def check_if_isdigit(value):
    if value == None:
        return False
    elif value.isdigit() == True:
        return True
    else:
        return False

times = None
a4i = {}

while check_if_isdigit(times) == False:
    times = ask4input("How many numbers you wish to introduce in order me to compare it with the last number: ")
else:
    for item in range(1, (int(times)+1)):
        a4i[item] = ask4input("I need a number: ")
        while check_if_isdigit(a4i[item]) == False or minimum_lenght(a4i[item]) == False:
            print("False!, oh noes dat no good :(")
            a4i[item] = ask4input("I need a JUST and/or MORE numbers: ")
        else:
            continue

while ((alpha = ask4input('test')) == False):
    # print("it worked")
    x = alfa;

# print(a4i)

for item in range(1, int(times)+1):
    if a4i[item] == a4i[int(times)]:
        print("found it!")
        print("Your value is: {}".format(a4i[item]))
        print("Your value was in {} place.".format(item))
    else:
        print("{} is a -> sad llama, drama llama".format(a4i[item]))
        continue