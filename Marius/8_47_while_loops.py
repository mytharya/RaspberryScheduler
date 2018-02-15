#8_47 while loops

"""
while cond:
    code.....
"""

#1st varinat of a loop
num = 1

while num <= 10:
    print ("loop number {} .".format(num))
    num = num +1

#2nd variant of a loop
num1 = 1

while num1 <= 10:
    if num1 % 2 != 0:
        print ("Your numer is : ", num1)
    num1 = num1 + 1

#3rd variant of a loop
L = []

while len (L) < 5:
    new_name = input ("Please add a new name: ").strip().capitalize()
    L.append(new_name)
print ("Sorry list is full")
print ("You have this many names in list: ",L)
