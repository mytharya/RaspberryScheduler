# w3resources-10
# Write a Python program to print the documents (syntax, description etc.) of Python built-in function(s).

while True:
    try:
        value = input('Enter name of a PYTHON built-in function : ')
        break
    except:
        print("That's not a number!")

# my variant
print(eval(value).__doc__)

# official variant
print (int.__doc__)