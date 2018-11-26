# w3resources-22
# Write a Python program to count the number 4 in a given list.

def ask4input():
    while True:
        global valu3
        try:
            valu3 = int(input("Input some numbers and i'll count how many times there is a 4: "))
            break
        except:
            print("thats a NO NO, mister!")

def do_the_thingy():
    global found_a_4
    found_a_4 = 0
    for number in str(valu3):
        print("The number is: ",number)
        if int(number) == 4:
            found_a_4 += 1
        # else:
        #     continue

ask4input()
# print(valu3)
# print(type(valu3))
do_the_thingy()

print("I've found {} time(s) number 4 (four)!".format(found_a_4))