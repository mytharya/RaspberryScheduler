# w3resources-16
# Write a Python program to get the difference between a given number and 17, if the number is greater than 17 return double the absolute difference.

values = {'first':None, 'second':None}

def ask4input(place):
    while True:
        try:
            global value
            value = int(input('Enter {} poizitive numeric value: '.format(place)))
            break
        except:
            print('NO NO NO sir! thats not descifrable')

def program_start():
    for key in values:
        ask4input(key)
        values[key] = value

def get_all_keys_in_dict():
    global keyz
    keyz = list(values.keys())
    # print(keyz)
    # return keyz

def compare_values():
    if values[keyz[0]] > values[keyz[0+1]]:
        return values[keyz[0]] - values[keyz[0+1]]
    else:
        return values[keyz[0+1]] - values[keyz[0]]

def print_result(result):
    print(result)

program_start()
get_all_keys_in_dict()
print_result(compare_values())

# print(diff)

print('meh!')