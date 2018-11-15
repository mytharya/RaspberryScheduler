# w3resources-18
# Write a Python program to calculate the sum of three given numbers, if the values are equal then return thrice of their sum.

values = {'first':None,'second':None,'third':None}

global keyz

def ask4input(place):
    while True:
        try:
            return int(input('Enter {} value: '.format(place)))
        except:
            print('dat NOT compute!')

def save_value_into_its_place(key, value):
    values[key] = value

def place_holder():
    for key in values:
        save_value_into_its_place(key, ask4input(key))

def make_a_list_of_indexes_from_a_dict(dict_name):
    global keyz
    keyz = list(values.keys())

def compare_values_of_dict():
    if values[keyz[0]] == values[keyz[1]] == values[keyz[2]]:
        return (values[keyz[0]] + values[keyz[1]] + values[keyz[2]])*3
    else:
        return values[keyz[0]] + values[keyz[1]] + values[keyz[2]]

# print values.keys()
# print values.values()
# print values.items()

# print(len(values))
# print(len(values.keys()))

# print(values(key))
# for len(values[key]) in values:
#     print(key[])
#     if 0 < key and key < len(values):
#         print(key)

place_holder()
# print(type(values.keys()))
make_a_list_of_indexes_from_a_dict(values)
print(compare_values_of_dict())

# print('_'*60)
# print(keyz[0])
# print(values.keys())

# print(len(values.keys()))

# kk = 0
# if kk < len(values.keys()):

# while kk < len(values.keys()):
#     print(kk)
#     kk += 1
#     print(values[keyz[0]])

# for keyxx in values.keys():
#     print(keyxx)

print('wait! is it k?')