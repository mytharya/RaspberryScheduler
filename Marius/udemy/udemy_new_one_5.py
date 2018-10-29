# working with files
hosts = open('c:\windows\system32\drivers\etc\hosts')

print('The current position: {}'.format(hosts.tell()))
hosts_file_contents = hosts.read()
print(hosts_file_contents) 
print('The current position: {}'.format(hosts.tell()))
# print(hosts.read())
hosts.seek(0)
print('The current position: {}'.format(hosts.tell()))
# print(hosts.read())

# Close file after open
print()
print('File closed? {}'.format(hosts.closed))
if not hosts.closed:
    hosts.close()
print('File closed? {}'.format(hosts.closed))

# Automatic closing of a file after read
print('Start reading the file')
with open('c:\windows\system32\drivers\etc\hosts') as hosts:
    print('File closed? {}'.format(hosts.closed))
    print(hosts.read())
print('Finished reading the file.')
print('File closed? {}'.format(hosts.closed))

# 
with open('test.txt') as the_file:
    for line in the_file:
        print(line.rstrip())
    print(the_file.mode)

# lets write smtg to the file
with open('test.txt', 'a') as the_file:
    the_file.write('\n')
    the_file.write('This is smtg that it should go into the file.\n')
    the_file.write("Here's more.\n")
with open('test.txt') as the_file:
    print(the_file.read())

