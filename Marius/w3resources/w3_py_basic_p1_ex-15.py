# w3resources-15
# Write a Python program to get the volume of a sphere with radius 6

# my variant
import math

def ask4input():
    while True:
        try:
            global radius
            radius = int(input('\nEnter a radius from which i will calculate the volume of a sphere: '))
            break
        except:
            print("\nle'in-put is not the 'right-size' (ahem...)")

ask4input()

volume = (4/3) * math.pi * (radius * radius * radius)
print(volume)
# or
print((4/3) * math.pi * (radius * radius * radius))

# le' officiel variant(e)