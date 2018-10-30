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

for key in values:
    ask4input(key)
    values[key] = value

def all_keys_in_dict():
    keyz = list(values.keys())
    # print(keyz)

all_keys_in_dict
print(values(keyz(0)))

# def compare_values():
#     for key in values:
#         values[keyz[0]] <

print('meh!')