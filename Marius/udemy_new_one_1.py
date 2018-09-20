def separation():
    #Separation line
    print ( "_" * 100)

def nl(nl_n=1):
    """Cleans up the screen with a number of lines"""
    #New line x times
    print ("\n" * nl_n)

def clean_up():
    separation()
    nl(15)

def odd_or_even(number):
    """Determine is a number is odd or even."""
    if number % 2 == 0:
        return 'Even'
    else:
        return 'Odd'

def say_hi(text, number):
    """Say a text to get displayed."""
    print("Hi {} and your number is {}!".format(text, number))

def get_name():
    nl()
    name = input('What\'s your name?: ')
    return name

def display_name(name):
    nl()
    print('Your name is: {}'.format(name))

def get_and_say_name():
    """ This function gets_name and displays_name"""
    name = get_name()
    display_name(name)

#call help of a custom function if function has  """Function help""" defined
#help(say_hi)

clean_up()
odd_or_even_string = odd_or_even(7)
print(odd_or_even_string)
nl()
say_hi('yo mama so fat!', odd_or_even_string)
nl()
get_and_say_name()