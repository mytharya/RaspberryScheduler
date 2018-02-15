#9_60 packing and unpacking

#just prints stuff
print (1,2,3,4,5,"\n")

#list of numbers
numbers = [1,2,3,4,5]
print(numbers,"\n")

#list unpacking
print(*numbers,"\n")

#strings
print ("abc","\n")
print (*"abc","\n")
print ("a","b","c","\n")

#definition
def add (x,y):
    return x+y

print(add(10,10))

#new one
def addd (*numbers):
    total = 0
    for number in numbers:
        total = total + number
    return(total)
print()
print(addd(1,2,3,4,5,6,7,8,9))

#new one again
def about(name,age,likes):
    sentence = "\nMeet {}! They are {} years old and they like {}.\n".format(name,age,likes)
    return sentence

dictionary={"age":23,"name":"Ziyad","likes":"Python"}

print(about(**dictionary))
#       * pack unpack   iterables, tuples, functions, pack uncpack
#new    **pack unpack   **key word arguments**
def foo(**kwargs):
    for key, value in kwargs.items():
                print("{}:{}".format(key, value))

print(foo(huda = "Female", Ziyad="male"))
