# w3resources-29
# Write a Python program to print out a set containing all the colors from color_list_1 which are not present in color_list_2.
# Test Data : 
# color_list_1 = set(["White", "Black", "Red"]) 
# color_list_2 = set(["Red", "Green"])
# Expected Output : 
# {'Black', 'White'}

# color_list_3 = color_list_1.difference(color_list_2)
# print(color_list_3)

import timeit

# color1 = temp1 = list(range(100))
# color2 = [i * 2 for i in range(50)]
# init = temp1 = list(range(100)); temp2 = [i * 2 for i in range(50)]
temp1 = list(range(99))
temp2 = [i * 2 for i in range(50)]

print (timeit.timeit(temp2.difference(temp1)))