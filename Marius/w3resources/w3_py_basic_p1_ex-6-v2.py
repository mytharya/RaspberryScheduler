# w3resources-6
# Write a Python program which accepts a sequence of comma-separated numbers from user and generate a list and a tuple with those numbers.
value_list = []
value_tuple = ()
index_value = 0

value = input('Enter at least 4 vaules (all-in-one) separated by commas: ')
for element in value:
    try:
        element = int(element)
    except:
        continue
    
    if type(element) is int:
        index_value = index_value + 1
        value_list.append(element)
        value_tuple = value_tuple + (element,)

print('Your lists contains these elements: {}'.format(value_list))
print('Your tuple contains these elements: {}'.format(value_tuple))