# Ask user for name
print("="*1)
name = input("What is your name?: ")

# Ask user for thei age
print("="*1)
age = input("What is your age?: ")

# Ask user for their city
print("="*1)
city = input("What is your city?: ")

# Ask user what they enjoy
print("="*1)
love = input ("What do you love doing?: ")

# Create output text
print("="*1)
string = "Your name is {} and you are {} years old. You live in {} and you love {}."
output = string.format(name, age, city, love)

# Print output to screen
print ("="*40)
print (output)
print ("isnt that l0al?")
