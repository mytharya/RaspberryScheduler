
print('hello world')

x = "testing"

y = 1 + 2

# a = float(input("Enter a number: "))
# b = float(input("Enter another number: "))
# print(a+b)

spam = 7;

if spam > 3:
    if spam > 5:
        print("Bigger than 5")
    else:
        print("test")
elif spam < 0 or spam > 1:
    print("Smaller than 0 or bigger than 1")
elif not (1 + 2 == 3):
    print("false")

i=1
while i<=5:
    print(i)
    i += 1;

print("Finished")

i=0
while 1==1:
    if i == 5:
        continue
    if i > 2:
        break
    else:
        print("in the loop")
    i += 1

#lists
words = ["hello", "world", "!"]
print(words[0])
print (words)

print("World in words: ") 
print("world" in words)

empty_list = []
print(empty_list)

number = "super"
things = ["string", 0, [1, 2, number], 4.56]

if 4.56 in things:
    print(things[0])

print(things[2][2])

nums = [1, 2, 3]
print(nums + [4, 5, 6])
print(nums * 2)

nums = [1, 2, 3]
nums.append(4)
print(nums)
print(len(nums))

nums.insert(1, 5)
print(nums)

print(nums.index(3))
nums.append(3)
print(nums.index(3))
print(nums.count(3))

numbers = list(range(10))
print(numbers)

numbers = list(range(2, 5))
print(numbers)

numbers = list(range(5, 20, 2))
print(numbers)

#loops
words = ["hello", "world", "spam", "eggs"]
counter = 0
max_index = len(words) - 1

while counter <=max_index:
    word = words[counter]
    print(word + "!")
    counter += 1

for word in words:
    print(word + "!!")

for i in range(4):
    print(words[i])

#calculator

while True:
    print("Options")
    print("Enter 'add' to add two numbers")
    print("Enter 'substract' to substract two numbers")
    print("Enter 'multiply' to multiply two numbers")
    print("Enter 'divide' to divide two numbers")
    print("Enter 'exit' to end the program")
    user_input = input(": ")

    if user_input == "exit":
        break
    
    elif user_input == "add":
        num1 = float(input("Enter a number: "))
        num2 = float(input("Enter another number: "))
        result = str(num1 + num2)
        print("The answer is " + result)

    else:
        print("Unknown input")

