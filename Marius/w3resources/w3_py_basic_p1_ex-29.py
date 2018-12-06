# w3resources-29
# Write a Python program to print out a set containing all the colors from color_list_1 which are not present in color_list_2.
# Test Data : 
color_list_1 = set(["White", "Black", "Red"]) 
color_list_2 = set(["Red", "Green"])
# Expected Output : 
# {'Black', 'White'}

color_list_3 = color_list_2.difference(color_list_1)
color_list_4 = color_list_1.difference(color_list_2)

print("Your 1st list contains {} colors. ".format(color_list_1))
print("Your 2st list contains {} colors. ".format(color_list_2))
print("The missing colors in 1st list are: {}.".format(color_list_3))
print("The missing colors in 2nd list are: {}.".format(color_list_4))