def separation(separation_nr_of_times=100):
    """ usage: separation(separation_nr_of_times) (default separation_nr_of_times=100)"""
    print('_' * separation_nr_of_times)
## lists
## defines a list
# list_name = [item_1, item_2, item_N]
## emplty list
# list_name = []
## list by index
# list_name[index]
# another example
help(separation)
animals = ['man', 'bear', 'pig']
print(animals)
print(animals[0])
animals[0]= 'cat'
print(animals)
print(animals[0])
# print stuff in reverse
separation()
print(animals[-1])
print(animals[-2])
# add single item to list
separation()
print(animals)
animals.append('cow')
print(animals[-1])
print(animals)
# add multiple items to list
separation()
print(animals)
animals.extend(['cangaroo', 'dog'])
print(animals)
# add another way
separation()
more_animals = ['bee', 'bear']
animals.extend(more_animals)
print(animals)
# insert into list at certain location
separation()
animals.insert(0, 'horse')
print(animals)
separation()
animals.insert(2, 'duck')
print(animals)
"""     SLICES      """
separation()
# list[index1:indexN]
# list[:indexN]
# list[index1:]
print(animals)
some_animals = animals[1:4]
print('This is a slice of animals[1:4] = {}'.format(some_animals))
first_two = animals[0:2]
print('First two animals: {}'.format(first_two))
first_two_again = animals[:2]
print('First two again: {}'.format(first_two_again))
separation()
last_two = animals[4:6]
print('Last two animals: {}'.format(last_two))
last_two_again = animals[-2:]
print('Last two again: {}'.format(last_two_again))
separation()
part_of_a_horse = 'horse'[1:3]
print(part_of_a_horse)
separation()
bear_index = animals.index('bear')
print(bear_index)
separation()
""" Exception handling """
try:
    unicorn_index = animals.index('unicorn')
except:
    unicorn_index = 'No unicorn(s) found.'

print(unicorn_index)
separation()
""" LoopS """
# for item_variable in list_name:
#   Code block
for animal in animals:
    print(animal.upper())
separation()
# while conditionS:
#   Code block
index = 0

while index < len(animals):
    print(animals[index])
    index += 1
separation()
""" Sort method """
sorted_animals = sorted(animals)
print('Animal list: {}'.format(animals))
print('Sorted animal list: {}'.format(sorted_animals))
animals.sort()
print('Animals after sort method: {}'.format(animals))
separation()
""" Concatenate """
more_animals = ['goose', 'ceetah', 'elephant']
all_animals = animals + more_animals
print(all_animals)
separation()
""" len """
print(len(animals))
animals.append('monkey')
print(len(animals))
separation()
""" Range """
#range of given number
for number in range(3):
    print(number)
separation()
#range with start and stop
for number in range(1,3):
    print(number)
separation()
# range with step
for number in range(1,10,2):
    print(number)
separation()
#example
for number in range(0, len(animals), 2):
    print(animals[number])
separation()
