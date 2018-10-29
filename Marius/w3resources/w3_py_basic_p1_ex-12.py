# w3resources-12
# Write a Python program to print the calendar of a given month and year. Note : Use 'calendar' module. 

import calendar

while True:
    try:
        year = int(input('Enter a year: '))
        month = int(input('Enter a month: '))
        break
    except:
        print('This is not a year or a month! Try again.')

print(calendar.month(year,month))