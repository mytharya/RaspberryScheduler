def nl(number):
    # new line X times
    print('\n' * number)

def line(number):
    # line X times
    print('_' * number)

nl(20)
line(120)

# w3resources-1
# Write a Python program to print the following string in a specific format (see the output).
# Sample String : "Twinkle, twinkle, little star, How I wonder what you are! Up above the world so high, Like a diamond in the sky. Twinkle, twinkle, little star, How I wonder what you are"
# Twinkle, twinkle, little star,
# 	How I wonder what you are! 
# 		Up above the world so high,   		
# 		Like a diamond in the sky. 
# Twinkle, twinkle, little star, 
# 	How I wonder what you are

print('\n\nTwinkle, twinkle, little star,\n\tHow I wonder what you are!\n\t\tUp above the world so high,\n\t\tLike a diamond in the sky.\nTwinkle, twinkle, little star,\n\tHow I wonder what you are...\n')
line(120)

# w3resources-2
# Write a Python program to get the Python version you are using.

import sys
print(sys.version,'\n')
print(sys.version_info,'\n')
line(120)

# w3resources-3
# Write a Python program to display the current date and time.
import datetime
print('The date and time is: ', datetime.datetime.now())
print('The year is: ', datetime.datetime.now().year)
print('The month is: ', datetime.datetime.now().month)
print('The day is: ', datetime.datetime.now().day)
print('The hour is: ', datetime.datetime.now().hour)
print('The minute is: ', datetime.datetime.now().minute)
print('The second is: ', datetime.datetime.now().second)
print('The microsecond is: ', datetime.datetime.now().microsecond)
line(120)

# w3resources-4
# Write a Python program which accepts the radius of a circle from the user and compute the area.
import math
while True:
    try:
        # radius = int(input('Enter radius of circle: '))
        radius = 6
        break
    except:
        print('Thats a non-computable value! Try again :)')

circle_area = math.pi*(radius**2)
print(circle_area)
line(120)

# w3resources-5
# Write a Python program which accepts the user's first and last name and print them in reverse order with a space between them.
while True:
    # name = input('Enter your complete name: ')
    name = 'Mike'
    char_isdigit = False
    for char in name:
        if char.isdigit():
            print('Thats a not a name! Try again :)')
            char_isdigit = True
            break
    if char_isdigit == False:
        print(name[::-1])
        break
line(120)