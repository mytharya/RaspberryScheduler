# Ditionaries
# defined dictionary
contacts = {'Jason':'555-0123', 'Carl':'555-0987'}
# asign to variables dictionay contents
jasons_phone = contacts['Jason']
carls_phone = contacts['Carl']
# print variable from dictionary
print('Dial {} to call Jason'.format(jasons_phone))
print('Dial {} to call Carl'.format(carls_phone))
# change value from dictionary
contacts['Jason'] = '555-0000'
# re-assign variable value from dictionary
jasons_phone = contacts['Jason']
# print the modified value from dictionary
print('Dial {} to call Jason'.format(jasons_phone))
# add new variable to dictionary
print(contacts)
print(len(contacts))
contacts['Tony'] = '555-0570'
print(len(contacts))
print(contacts)
# remove/delete variables from dictionary
print(contacts)
del contacts['Jason']
print(contacts)
# value for keys can be lists in dictionaries
contacts['Mike'] = ['555-0999', '555-0888']
print(contacts)
print(contacts['Mike'][1])
# for loop to print all variabiles asigned to a number
for number in contacts['Mike']:
    print('Phone: {}'.format(number))
# ifs to test stuff
if 'Mike' in contacts.keys():
    print('Mikes phone number is: ')
    print(contacts['Mike'][0])
# if for something that does not exist
if 'Jason' in contacts.keys():
    print('Jasons phone number is: ')
    print(contacts['Jason'][0])
#check if a value is in a dictionary
print('555-0570' in contacts.values())
# for loop
for contact in contacts:
    print('The number for {0} is {1}.'.format(contact, contacts[contact]))
# double variable loop
for person, phone_number in contacts.items():
    print('The number for {0} is {1}.'.format(person, phone_number))
# nesting (dictionaries)
contacts['Spock'] = {'phone':'555-0555', 'email':'q@q.com'}
print(contacts)
print(contacts['Spock'])
for contact in contacts:
    print('_' * 100)
    print("{}'s contact info: ".format(contact))
    try:
        if 'phone' or 'email' in contacts.items():
            print(contacts[contact]['phone'])
            print(contacts[contact]['email'])
    except:
        print('{} doesent have a phone or a email.'.format(contact))
print('_' * 100)
for contact in contacts.items():
    print (contact)
    #print ('{} has these: {}'.format(contact, contacts[contact]))
#if value in contacts.values():
#    print(value)

