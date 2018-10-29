# w3resources-7
# Write a Python program to accept a filename from the user and print the extension of that.

filename = input('Please input any filename in order to find extension: ')

# variianta 1
# char_loc = filename.find('.')
# print(filename[char_loc+1:])

# varianta 2
print(filename[filename.find('.')+1:])
