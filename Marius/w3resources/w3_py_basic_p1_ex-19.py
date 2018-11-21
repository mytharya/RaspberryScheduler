# w3resources-19
# Write a Python program to get a new string from a given string where "Is" has been added to the front.
# If the given string already begins with "Is" then return the string unchanged.

def ask4input():
    while True:
        try:
            global value
            value = str(input('Give me some text: '))
            break
        except:
            print("oh noes! noes vowels for yous!")

def compare_input(value):
    nv = value[0] + value[1]
    # print(nv.lower())
    if nv.lower() == 'is':
        print('YouZ gotZ BIG "IsZ" in textZ and is the 1st word!')
    else:
        new_value = 'Is ' + value
        print(new_value)

ask4input()
# print('value: ',value)
compare_input(value)
# print(type(value))