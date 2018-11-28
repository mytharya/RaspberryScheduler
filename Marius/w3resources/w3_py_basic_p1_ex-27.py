# w3resources-27
# Write a Python program to concatenate all elements in a list into a string and return it.

def ask4input(question):
    return input(question)

times = ask4input("How many concatenations you wish to make?: ")
# print(times)
for x in range(1, (int(times)+1)):
    if x == 1:
        value_x = ask4input("Please enter the {}st value: ".format(x))
    elif x == 2:
        value_x = ask4input("Please enter the {}nd value: ".format(x))
    elif x == 3:
        value_x = ask4input("Please enter the {}rd value: ".format(x))
    else:
        value_x = ask4input("Please enter the {}th value: ".format(x))

for x in range(1, (int(times)+1)):
    concatenated_value = None
    concatenated_value = concatenated_value + value_x

print(concatenated_value)