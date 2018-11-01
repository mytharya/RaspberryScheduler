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
    if keyz[0] == keyz[1] == keyz[2]:
        return (keyz[0] + keyz[1] + keyz[2])*3
    else:
        return keyz[0] + keyz[1] + keyz[2]
    
place_holder()
print(keyz)
# print(compare_values_of_dict())

print(values)
print('wait! is it k?')