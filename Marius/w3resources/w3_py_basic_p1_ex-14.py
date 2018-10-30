# w3resources-14
# Write a Python program to calculate number of days between two dates.

import calendar
import datetime

first_date = []
second_date = []

print("I calculate the number of days between two dates")

def check_if_dates_have_data(name):
    if len(name) == 0:
        ask4input(name, 'year')
        ask4input(name, 'month')
        ask4input(name, 'day')
    else:
        None

def check_if_is_ymd(name, place, date):
    """check if input is year, month or day"""
    if place == 'year':
        if 0 < date:
            # print('good year')
            name.append(date)
            # return Breakpoint()
        else:
            None
            # print('bad year')
            return Break
    elif place == 'month':
        if 0 < date < 13:
            # print('good month')
            name.append(date)
        else:
            None
            # print('bad month')
    else:
        if 0 < date <= calendar.monthrange(first_date[0], first_date[1])[1]:
            # print('good day')
            name.append(date)
        else:
            None
            # print('bad day')

def ask4input(name, place):
    while True:
        try:
            date = int(input('Enter {} {}: '.format(name, place)))
            check_if_is_ymd(name, place, date)
            # print(name)
            
            if place == 'year':
                ph = 0
            elif place == 'month':
                ph = 1
            else:
                ph = 2

            if name[ph] == date:
                break
            else:
                None
        except:
            print("dat' does not compute! try again.")

def compare_dates(a, b):
    global the_difference_is
    if datetime.date(a[0],a[1],a[2]) < datetime.date(b[0],b[1],b[2]):
        the_difference_is = (datetime.date(b[0],b[1],b[2]) - datetime.date(a[0],a[1],a[2]))
    else:
        the_difference_is = (datetime.date(a[0],a[1],a[2]) - datetime.date(b[0],b[1],b[2]))

check_if_dates_have_data(first_date)
check_if_dates_have_data(second_date)

compare_dates(first_date,second_date)
print(the_difference_is.days)
print('k')