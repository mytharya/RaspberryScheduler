# w3resources-19
# Write a Python program to get a new string from a given string where "Is" has been added to the front.
# If the given string already begins with "Is" then return the string unchanged.

def ask4input():
    while True:
        try:
            global value
            value = str(input('Give me some text: '))
            break
        except:
            print("oh noes! noes vowels for yous!")

ask4input()
if 'Is' in value:
    print ('There is not "Is" in!')
else:
    new_value = 'Is ' + value


print(new_value)