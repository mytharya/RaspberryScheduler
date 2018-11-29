# w3resources-27
# Write a Python program to concatenate all elements in a list into a string and return it.

value = {}

def ask4input(question):
    return input(question)

def ask4inputNtimes(times):
    for x in range(1, (int(times)+1)):
        if x == 1:
            value[x] = ask4input("Please enter the {}st value: ".format(x))
        elif x == 2:
            value[x] = ask4input("Please enter the {}nd value: ".format(x))
        elif x == 3:
            value[x] = ask4input("Please enter the {}rd value: ".format(x))
        else:
            value[x] = ask4input("Please enter the {}th value: ".format(x))

def concatenate_values():
    concatenated_value = None
    for x in value:
        if concatenated_value == None:
            concatenated_value = value[x]
        else:
            concatenated_value = concatenated_value + value[x]
    return concatenated_value

times = ask4input("How many concatenations you wish to make?: ")
ask4inputNtimes(times)
concatenated_value = concatenate_values()
print(concatenated_value)