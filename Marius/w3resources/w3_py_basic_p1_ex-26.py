# w3resources-26
# Write a Python program to create a histogram from a given list of integers.

def histogram(items):
    for item in items:
        print("*" * item)


histogram([6,5,3,0,0,8,6,4,2,6,2,4])