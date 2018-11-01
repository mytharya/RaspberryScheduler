# w3resources-17
# Write a Python program to test whether a number is within 100 of 1000 or 2000

def ask4input(place):
    while True:
        try:
            return int(input('Input {} value: '.format(place)))
        except:
            print('uh-oh!')

first = ask4input('first')
second = ask4input('second')

first_diff = abs(1000 - first) <= 100
second_diff = abs(2000 - second) <= 100

diff = first_diff or second_diff

# diff = (abs(1000 - first) <= 100) or (abs(2000 - second) <= 100)
print('\nfirst_diff is: ',first_diff)
print('\nsecond_diff is:',second_diff)
print('\ndiff (first_diff OR second_diff) is:',diff)

print('\nk')