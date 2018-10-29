# tuples
days_of_the_week = ('Monday', 'Tuesday', 'Wednessday', 'Thursday', 'Friday', 'Saturady', 'Sunday')
monday = days_of_the_week[0]
print(monday)
print()

for day in days_of_the_week:
    print(day)

# tuple to list and back - conversion
print()
weekend_tuple = ('Saturday', 'Sunday')
weekend_list = list(weekend_tuple)
print('weekend_tuple is {}'.format(type(weekend_tuple)))
print('weekend_list is {}'.format(type(weekend_list)))

# asign multiple values to varabiles at once
print()
(sat, sun) = weekend_tuple
print(sat)
print(sun)

# tuple asignment with lists
print()
contact_info = ['555-0123', 'q@q.com']
phone, email = contact_info
print(phone)
print(email)

# Tuples
print()
def high_and_low(numbers):
    """ Determines the highest and the lowest number. """
    highest = max(numbers)
    lowest = min(numbers)
    from statistics import median as median
    average = median(numbers)
    return (highest, average, lowest)

lottery_numbers = [16, 4, 42, 15, 23, 8]
(highest, average, lowest) = high_and_low(lottery_numbers)
print('The highest number is: {}'.format(highest))
print('The average is: {}'.format(average))
print('The lowest number is: {}'.format(lowest))

# Tuple asignment in a for loop
print()
contacts = [('Jason', '555-0123'), ('Carl', '555-0987')]
for (name, phone) in contacts:
    print("{}'s phone number is {}.".format(name, phone))

# delete a tuple
del contacts
