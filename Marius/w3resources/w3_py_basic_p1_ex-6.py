# w3resources-6
# Write a Python program which accepts a sequence of comma-separated numbers from user and generate a list and a tuple with those numbers.
value_list = []
value_tuple = ()
index_value = 0
while index_value <=2:
    try:
        value = int(input('Enter at least 4 vaules (one-by-one): '))
        if type(value) is int:
            index_value = index_value + 1
            if index_value == 1:
                print('Your {}st number is : {} .'.format(index_value, value))
            elif index_value == 2:
                print('Your {}nd number is : {} .'.format(index_value, value))
            elif index_value == 3:
                print('Your {}rd number is : {} .'.format(index_value,value))
            else:
                print('Your {}th number is : {} .'.format(index_value,value))
            value_list.append(value)
            value_tuple = value_tuple + (value,)
    except:
        print('Thats not a number! Keep trying :)')

print('Your lists contains these elements: {}'.format(value_list))
print('Your tuple contains these elements: {}'.format(value_tuple))