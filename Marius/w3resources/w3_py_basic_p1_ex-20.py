# w3resources-20
# Write a Python program to get a string which is n (non-negative integer) copies of a given string.

def ask4input():
    while True:
        try:
            global value
            value = str(input("Gimmie sum sum (string) and i'll copy it 3 times: "))
            break
        except:
            print("oh noes, youZ hasZ notZ gotZ itZ!")

def do_the_thingy():
    if len(value) >= 0:
        print((value + ".") * len(value))

ask4input()
do_the_thingy()