# w3resources-16
# Write a Python program to get the difference between a given number and 17, if the number is greater than 17 return double the absolute difference.

def ask4input(place):
    while True:
        try:
            value = int(input('Enter {} poizitive numeric value: '.format(place)))
            break
        except:
            print('NO NO NO sir! thats not descifrable')

values = {'first':None, 'second':None}

for key in values:
    print(key)
    ask4input(key)

# ask4input(first)
# ask4input(second)
print('meh!4')